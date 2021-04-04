from ..context_manager import context, parent, this
from ..context_manager.uid_system import UID, gen_id, id_ref


class BaseComponent:
    """
    Notes:
        see `WebPage:docstring:PythonMixin注意事项`
    """
    level: int
    uid: UID
    
    # parent: None
    # children: list['BaseComponent']
    
    @staticmethod
    def _get_level(frame) -> int:
        """
        DELETE: no usage
        
        Notes:
            请确保 BaseComponent 在实例化的时候, 与 with 语句处于同一行! 否则将
            导致层级计算错误.
            举例来说, 如下所示:
                # 正确
                with BaseComponent() as com:
                    ...
                # 错误 (不要使用 \\ 换行!) (注: 这里我是想用单反斜杠表示的, 但是
                # 会导致 python 在解析本模块时报错, 所以用双反斜杠暂代)
                with \\
                    BaseComponent() as com:
                    ...
                
        Returns:
            int 0|4|8|12|...
                数字越大, 嵌套越深; 数字越小, 越接近根层级. 0 代表顶级节点 (通常
                是 WebPage 对象).
        """
        from ..context_manager.inspect import inspect
        inspect.chfile(frame.f_code.co_filename)
        srcln = inspect.get_line(frame.f_lineno)
        spacing = len(srcln) - len(srcln.lstrip())
        return int(spacing / 4)
    
    def __enter__(self):
        # self.parent = None
        # self.children = []
        
        # for now, `this` keyword represents 'the last' component (usually it
        # means 'parent' component), so we get the last component's real body
        # by `this.represents`
        last_com = this.represents  # type: [BaseComponent, None]
        
        self.level = last_com.level + 4 if last_com is not None else 0
        # from lk_utils.lk_logger import lk
        # lk.loga(last_com, self.level)
        self.uid = gen_id(self.level)
        
        context.update(self.uid, self.level, self, last_com)
        #   after `context.update`, `this` and `parent` now work as expected.
        #   i.e. now `this` represents `self`, and `parent` represents `last_com`
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """ 将 this, parent 分别指向 parent 和 grand_parent. """
        if parent.represents is not None:
            this.represents.add_to(parent.represents)
        
        this.point_to(id_ref[(pid := self.uid.parent_id)])
        parent.point_to(id_ref[pid.parent_id] if pid else None)

from lk_logger import lk

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
    
    _exit_lock: int
    
    #   0: 表示可退出
    #   >0: 表示当前不可退出 (此时会让 _exit_lock 计数减 1)
    #   see `justpy_declarative.hacking.ExitLockCount:docstring:作用机制`
    
    def __getattr__(self, item):
        if isinstance(item, str):
            if item.startswith('on_'):
                return lambda func: self.on(item[3:], func)
        # noinspection PyUnresolvedReferences
        return super().__getattr__(item)
    
    def __enter__(self):
        # self.parent = None
        # self.children = []
        from ..hacking import com_exit_lock
        self._exit_lock = com_exit_lock.fetch_lock()
        
        # for now, `this` keyword represents 'the last' component (usually it
        # means 'parent' component), so we get the last component's real body
        # by `this.represents`
        last_com = this.represents  # type: [BaseComponent, None]
        
        self.level = last_com.level + 4 if last_com is not None else 0
        self.uid = gen_id(self.level)
        lk.loga('enter', self.uid, h='parent')
        
        context.update(self.uid, self.level, self, last_com)
        #   after `context.update`, `this` and `parent` now work as expected.
        #   i.e. now `this` represents `self`, and `parent` represents `last_com`
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """ 将 this, parent 分别指向 parent 和 grand_parent. """
        if self._exit_lock > 0:
            self._exit_lock -= 1
            return
        
        lk.loga('exit', self.uid, h='parent')
        
        if parent.represents is not None:
            this.represents.add_to(parent.represents)
        
        this.point_to(id_ref[(pid := self.uid.parent_id)])
        parent.point_to(id_ref[pid.parent_id] if pid else None)

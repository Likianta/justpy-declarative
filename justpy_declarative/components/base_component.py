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
    #   see `ExitLockCount:docstring:作用机制`
    
    def __getattr__(self, item):
        if isinstance(item, str):
            if item.startswith('on_'):
                return lambda func: self.on(item[3:], func)
        # noinspection PyUnresolvedReferences
        return super().__getattr__(item)
    
    def __enter__(self):
        # self.parent = None
        # self.children = []
        global _com_exit_lock
        self._exit_lock = _com_exit_lock.fetch_lock()
        
        # for now, `this` keyword represents 'the last' component (usually it
        # means 'parent' component), so we get the last component's real body
        # by `this.represents`
        last_com = this.represents  # type: [BaseComponent, None]
        
        self.level = last_com.level + 1 if last_com is not None else 0
        self.uid = gen_id(self.level)
        lk.loga('enter', self.uid, self.level, h='parent')
        
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


class Build:
    """
    Examples:
        with WebPage() as page:
            with Build(add_main_text) as main_txt:
                main_txt.on('click', ...)
        
        def add_main_text():
            with Div() as div:
                with Text() as text:
                    return text
    """
    
    def __init__(self, build_func, *args, **kwargs):
        self._build = lambda: build_func(*args, **kwargs)
        self.view = None
    
    def __enter__(self):
        global _com_exit_lock
        _com_exit_lock.put_a_lock(1)
        #   see `ExitLockCount:docstring:作用机制`
        
        self.view = self._build()
        if self.view is None:
            self.view = this.represents
        assert self.view is not None
        # assert self.view is not None, (
        #     'You must call `return component` in the end of your `build_func`!'
        # )
        
        return self.view
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.view.__exit__(exc_type, exc_val, exc_tb)


class ComponentExitLock:
    """
    作用机制:
        TODO
    """
    
    _count = 0
    
    def fetch_lock(self):
        out = self._count
        self.reset_lock()
        return out
    
    def reset_lock(self):
        self._count = 0
    
    def put_a_lock(self, count: int):
        self._count = count


_com_exit_lock = ComponentExitLock()

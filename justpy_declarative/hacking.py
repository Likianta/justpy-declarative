class GlobalControl:
    exitable_cnt = 0
    #   可退计数器. see `components/__init__.py:Build.__enter__:docstring:可退计
    #   数器工作原理`
    #   当可退计数器为 0 时, `self.__exit__` 才能正常退出; 当可退计
    #   数器大于 0 时, 说明有外部控制器正在阻止本组件执行退出操作. 此时, 本组件
    #   不会退出, 而是把计数器减 1.
    #   see `self.__enter__:params:exitable_cnt`
    #       `self.__exit__`
    forbidden_exit = False
    #   see `components/base_component.py:BaseComponent:__exit__`
    #       `components/__init__.py:Build.__enter__`


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


com_exit_lock = ComponentExitLock()

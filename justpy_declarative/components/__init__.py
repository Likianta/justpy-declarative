from .html_components import *


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
        from ..hacking import com_exit_lock
        com_exit_lock.put_a_lock(1)
        #   see `justpy_declarative.hacking.ExitLockCount:docstring:作用机制`
        
        self.view = self._build()
        assert self.view is not None, (
            'You must call `return component` in the end of your `build_func`!',
        )
        
        return self.view
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.view.__exit__(exc_type, exc_val, exc_tb)

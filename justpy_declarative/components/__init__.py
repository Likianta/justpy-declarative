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
        self._build = lambda : build_func(*args, **kwargs)
        
    def __enter__(self):
        return self._build()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

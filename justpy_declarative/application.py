from .components import WebPage

from justpy_declarative.features import concurr


class Application:
    """
    Examples:
        with Application() as app:
            with WebPage() as page:
                ...
            app.start(page)
    """
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def start(self, page: WebPage, open_browser=True):
        if open_browser:
            self.open_browser('http://127.0.0.1:8000/')
        from justpy import justpy
        justpy(lambda: page)
    
    @concurr
    def open_browser(self, addr):
        from os import popen
        from time import sleep
        sleep(0.3)
        # FIXME: this command is only tested in Windows system
        popen(f'start {addr}')


def start(page: WebPage):
    app = Application()
    app.start(page)
    return app

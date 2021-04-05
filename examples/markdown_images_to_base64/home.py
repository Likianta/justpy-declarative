from justpy_declarative import *
from .address_bar import AddressBar
from .task_penel import TaskPanel


def main():
    with Application() as app:
        with WebPage() as homepage:
            homepage.body_classes = ('bg-gray-100')
            
            with Build(_app_win):
                pass
        
        app.start(homepage, open_browser=False)


def _app_win():
    with Div() as screen:
        screen.classes = 'flex items-center justify-center h-screen bg-gray-600'
        
        with Div() as win:
            win.classes = 'bg-gray-100 rounded-lg'
            win.style = 'width: 550px; height: 420px'
            
            with Build(_main_content):
                pass


def _main_content():
    with Div() as container:
        container.classes = ('flex-col')
        
        with AddressBar() as addr_bar:
            addr_bar.classes = (
                'mx-auto'
            )
            addr_bar.style = (
                'margin-top: 20px;'
                'width: 487px; height: 30px;'
            )
        
        with TaskPanel():
            pass

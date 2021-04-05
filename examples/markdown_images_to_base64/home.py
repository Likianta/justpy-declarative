from lk_lambdex import lambdex
from lk_logger import lk

from justpy_declarative import *


def main():
    with Application() as app:
        with WebPage() as homepage:
            homepage.body_classes = ('bg-gray-100')
            
            build_app_win()
        
        app.start(homepage, open_browser=False)


def build_app_win():
    with Div() as screen:
        screen.classes = 'flex items-center justify-center h-screen bg-gray-600'
        
        with Div() as win:
            win.classes = 'bg-gray-100 rounded-lg'
            win.style = 'width: 550px; height: 420px'
            
            build_main_content()


def build_main_content():
    with Div() as div:
        div.classes = ('flex')
        
        # row 1
        build_address_bar()
        
        # row 2
        # TODO


def build_address_bar():
    with Div() as addr_bar:
        addr_bar.classes = (
            'mx-auto'
        )
        addr_bar.style = (
            'margin-top: 20px;'
            'width: 487px; height: 30px;'
        )
        
        with Input() as inp:
            inp.classes = (
                'border-2 border-gray-300 '
                'placeholder-gray-300 text-blue-400 '
                'focus:border-blue-500'
            )  # note: justpy's tailwind css doesn't support `rounded-xl`
            inp.style = (
                'border-radius: 12px; border-top-right-radius: 0px; '
                'border-bottom-right-radius: 0px; '
                'float: left;'
                'padding-left: 16px; padding-right: 16px; '
                'width: 420px; height: 30px; '
            )
            
            inp.is_valid_path = False
            inp.placeholder = 'Select a markdown file to start...'
            
            inp.on_input(lambdex(('self', 'msg'), '''
                from os.path import exists
                self.is_valid_path = exists(self.value)
                print(
                    '[home.py:build_address_bar:inp:on_input]',
                    self.value, self.is_valid_path
                )
            '''))
        
        with Button() as btn:
            btn.classes = (
                'font-bold text-white'
            )
            btn.style = (
                'background-color: #6666CC;'
                'border-bottom-left-radius: 0;'
                'border-bottom-right-radius: 12px;'
                'border-top-left-radius: 0;'
                'border-top-right-radius: 12px;'
                'float: right; '
                'font-size: 13px;'
                'width: 67px; height: 30px;'
            )
            btn.text = 'BROWSE'


if __name__ == '__main__':
    main()
    lk.over()

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
            
            # return win


def build_main_content():
    with Div() as div:
        div.classes = ('flex')
        
        # row 1
        build_address_bar()
        
        lk.loga(div.uid, div.level)
        lk.loga(this.represents.uid, this.represents.level)
        
        with A() as a:
            raise Exception
        
        # TEST
        with Div() as test:
            raise Exception
            lk.loga(test.uid)
            test.style = (
                'background: #2f3640;'
                'position: absolute;'
                'top: 50%; left: 50%;'
                'height: 40px'
            )
            
            with Input() as inp:
                inp.style = (
                    'border-radius: 12px;'
                    'padding-left: 16px; padding-right: 48px;'
                    'width: 487px; height: 30px; float: left;'
                )
            
            with Button() as btn:
                btn.style = (
                    'height: 30px; float: right'
                )
                
                btn.text = 'BROWSE'
        
        # row 2
        # TODO


def build_address_bar():
    with Div() as addr_bar:
        addr_bar.classes = (
            'mx-auto'
        )
        
        with Input() as inp:
            inp.classes = (
                'border-2 border-gray-300 '
                'placeholder-gray-300 text-blue-400 '
                'focus:border-blue-500'
            )  # note: justpy's tailwind css doesn't support `rounded-xl`
            inp.style = (
                'border-radius: 12px;'
                'margin-top: 20px;'
                'padding-left: 16px; padding-right: 48px;'  # FIXME
                'width: 487px; height: 30px;'
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
            )
            btn.text = 'BROWSE'
        
        # return addr_bar


if __name__ == '__main__':
    main()
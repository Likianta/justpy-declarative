from lk_lambdex import lambdex

from justpy_declarative import *


class AddressBar(Div):
    
    def build(self):
        
        with Input() as inp:
            inp.classes = (
                'border-2 border-gray-300 '
                'placeholder-gray-300 text-blue-400 '
                'focus:border-blue-500 '
                'w-full h-full '
            )  # note: justpy's tailwind css doesn't support `rounded-xl`
            inp.style = (
                'border-radius: 12px; '
                'float: left;'
                'padding-left: 16px; padding-right: 16px; '
            )
            
            inp.is_valid_path = False
            inp.placeholder = 'Select a markdown file to start...'
            
            inp.on_input(lambdex(('self', 'msg'), '''
                from os.path import exists
                self.is_valid_path = exists(self.value)
                print(
                    '[home.py:_address_bar:inp:on_input]',
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
                'position: relative; bottom: 30px;'
                'width: 67px; height: 30px;'
            )
            btn.text = 'Browse'

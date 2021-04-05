from justpy_declarative import *


class LongButton(Div):
    
    # noinspection PyAttributeOutsideInit
    def build(self):
        self.style = (
            'width: 250px; height: 30px;'
            'background-color: #6666CC;'
            'border-radius: 12px;'
        )
        
        self.text = ''
        
        with Text() as txt:
            txt.classes = (
                'text-white '
            )
            txt.text = self.text  # FIXME
        
        with Icon() as icon:  # TODO
            pass

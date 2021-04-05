from justpy_declarative import *


class TaskPanel(Div):
    
    def build(self):
        self.classes = (
            'w-full h-auto '
            'bg-red-600'
        )
        self.style = (
            'display: flex;'
            'height: 300px;'
            'margin-top: 40px;'
        )

        with Card() as card_shadow:
            card_shadow.style += (
                'background-color: #CCCCCC;'
                'margin-left: 60px; margin-top: 28px;'
            )

            with Card() as card:
                card.style += (
                    'position: relative; right: 30px; bottom: 28px;'
                )
            

class Card(Div):
    
    def build(self):
        self.style = (
            'background-color: #6666CC;'
            'border-radius: 12px;'
            'width: 170px; height: 220px;'
        )

from lk_lambdex import lambdex

from justpy_declarative import Application, Div, WebPage

with Application() as app:
    with WebPage() as page:
        with Div() as div:
            div.text = 'Hello World'
            
            '''
            以下两种形式的 on_event 都支持
                div.on('click', lambda self, msg: ...)
                div.on_click(lambda self, msg: ...)
            '''
            
            div.on('click', lambdex(('self', 'msg'), '''
                self.text = 'Text Clicked'
            '''))
            
            div.on_mouseenter(lambdex(('self', 'msg'), '''
                self.text = 'Mouse Enter'
            '''))
            
            div.on_mouseleave(lambdex(('self', 'msg'), '''
                self.text = 'Mouse Leave'
            '''))
    
    app.start(page, open_browser=False)

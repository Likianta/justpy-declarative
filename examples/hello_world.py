from justpy_declarative import Application, WebPage, Div

with Application() as app:
    with WebPage() as page:
        with Div() as div:
            div.text = 'Hello World'
    app.start(page, open_browser=True)

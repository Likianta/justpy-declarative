# JustPy Declarative

`justpy-declarative` 是对 [`justpy`](https://justpy.io/) GUI库的封装.

`justpy-declarative` 旨在提供一种 "声明式" 的语法, 以更优雅的方式来创作 UI 组件树.

下面是一个 Hello World 代码, 方便您理解它的样子:

```python
from justpy_declarative import Application, WebPage, Div
from lk_lambdex import lambdex  # pip install lk-lambdex

with Application() as app:

    with WebPage() as page:

        with Div() as div:
            div.text = 'Hello World'
            div.on('click', lambdex(('self', 'msg'), '''
                self.text = 'Text was clicked!'
            '''))

    app.start(page, open_browser=True)
    #   This will automatically open `http://localhost:8000` in browser.

```

运行上面的代码, 您将在浏览器看到 "Hello World" 文字, 鼠标点击文字会变成 "Text was clicked!" 字样.

# 安装

通过 pip 安装:

```
pip install justpy-declarative
```

# 使用教程

`justpy-declarative` 的核心仍然是 justpy 库, 您可以在 [justpy 的官方文档](https://justpy.io/) 中学习; `justpy-declarative` 所特有的语法特性, 请查阅本项目下的 [tutorials](./tutorials) 目录.

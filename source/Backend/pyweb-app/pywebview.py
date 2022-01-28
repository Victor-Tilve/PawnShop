import webview

webview.create_window('LUZUMAR', 'http://127.0.0.1:8000/users/login/',fullscreen=True)
# webview.create_window('Hello world', 'https://pywebview.flowrl.com/',fullscreen=True)
webview.start(gui='qt')
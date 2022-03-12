import webview
webview.create_window('Luzumar', 'http://127.0.0.1:8000/users/login/',min_size=(1920, 1080))
# webview.create_window('Luzumar', 'http://127.0.0.1:8000/')
webview.start(http_server=True)
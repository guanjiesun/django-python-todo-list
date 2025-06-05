from django.http import HttpResponse


def set_cookie(request):
    """
    TODO 使用 response 添加删除 cookies
    """

    # 设置响应体
    body = """
    <html>
        <body style="text-align: center;">
            <h1>SETTING COOKIES</h1>
        </body>
    </html>
    """
    response = HttpResponse(content=body, content_type='text/html')

    # key是cookie的名字，value是cookie的值，max_age是cookie存活时间（秒）
    # TODO set_cookie 方法用于设置一个 cookie，最终会在响应头的字段 Set-Cookie 中体现
    response.set_cookie(key="name", value="guanjie sun", max_age=60)

    return response


def get_cookie(request):
    """
    TODO 使用 request 获取 cookie
    """

    # 设置响应体
    body = """
    <html>
        <body style="text-align: center;">
            <h1>GETTING COOKIES</h1>
        </body>
    </html>
    """
    response = HttpResponse(content=body, content_type='text/html')

    # 获取cookie，request.COOKIES 是一个字典对象
    print(request.COOKIES)

    return response


def delete_cookie(request):
    """
    TODO 使用 response 删除 cookie
    """

    # 设置响应体
    body = """
    <html>
        <body style="text-align: center;">
            <h1>DELETING COOKIES</h1>
        </body>
    </html>
    """

    response = HttpResponse(content=body, content_type='text/html')
    # 删除 set_cookie 视图函数中设置的 cookie
    response.delete_cookie(key="name")

    return response

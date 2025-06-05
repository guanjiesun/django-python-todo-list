import json
from pathlib import Path

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    """
    一个简单的测试函数
    """

    # 响应体
    html = """
    <html>
        <body style="text-align: center;">
            <h1>A SIMPLE TEST FUNCTION</h1>
        </body>
    </html>
    """

    return HttpResponse(html)


def save_query_params_2json(request):
    """
    如果查询参数不是空，将查询字符串中的参数保存在一个json文件中
    """
    # TODO request.GET 保存的是客户端通过 URL 查询字符串（query string）发送的所有请求参数（不局限于get请求方法）
    # ?key1=value1&key2=value2 是查询字符串的一般标准格式

    # 获取参数（QueryDict -> dict，保留所有值）
    query_params = dict(request.GET.lists())

    # 如果查询参数不是空，则将查询参数保存 json 文件
    if query_params:
        # 设置保存请求参数的文件路径
        current_file_path = Path(__file__)
        path = current_file_path.parent / "query_params.json"

        # 如果文件存在，加载已有数据
        if path.exists():
            with open(path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    # 即使文件存在，文件为空或者文件内容是非法json格式，则会触发 JSONDecodeError 异常
                    data = list()
        # 如果文件不存在，则新建一个空列表
        else:
            data = list()

        # 将查询字符串中的参数保存到 data 列表中
        data.append(query_params)

        # 写回文件，覆盖旧内容
        with open(path, "w") as file:
            # indent 参数将换行和缩进写入文件中
            # ensure_ascii = False 会保留原始字符 (如中文字符)
            json.dump(data, file, ensure_ascii=False, indent=4)
    else:
        print("QUERY PARAMETERS IS EMPTY")

    # 响应体
    html = """
    <html>
        <body style="text-align: center;">
            <h1>SAVING</h1>
            <h1>QUERY PARAMETERS</h1>
            <h1>TO</h1>
            <h1>JSON FILE</h1>
        </body>
    </html>
    """

    return HttpResponse(html)


def obtain_request_body(request):
    """
    TODO 获取post方法的请求体：直接使用request.POST
    TODO 获取其他请求方法的请求体：使用request.body然后解码（request.body返回的是字节序列）
    TODO 注意，一个函数中只能使用以上两种方法中的一个
    """

    # TODO request.POST 只能获取post请求体，不能获取patch和put请求体
    request_body = request.POST
    if request_body:
        print('*' * 15, 'REQUEST BODY', '*' * 15)
        for key in request_body.keys():
            print(f"{key}: {request_body.getlist(key)}")
        print('*' * 15, 'REQUEST BODY', '*' * 15, '\n')
    else:
        print("REQUEST BODY IS EMPTY")

    # TODO 如果查询参数不为空，也可以打印查询参数
    query_params = request.GET
    if query_params:
        print('*' * 15, 'QUERY PARAMETERS', '*' * 15)
        for key in query_params.keys():
            print(f"{key}: {query_params.getlist(key)}")
        print('*' * 15, 'QUERY PARAMETERS', '*' * 15, '\n')
    else:
        print("QUERY PARAMETERS IS EMPTY")

    # 响应体
    html = """
    <html>
        <body style="text-align: center;">
            <h1>OBTAIN </h1>
            <h1>REQUEST</h1>
            <h1>BODY</h1>
        </body>
    </html>
    """

    return HttpResponse(html)


def explore_request_headers(request):
    """
    探索请求头: request.META 或者 request.headers
    """

    # TODO request.Meta 包含请求头的信息、客户端信息和服务器端的信息
    # request.META 就是一个字典
    # if request.META:
    #     for key, value in request.META.items():
    #         print(f"{key}: {value}")

    # TODO request.headers 只包含请求头信息
    # request.header 是一个类似于字典的数据结构
    print('*' * 20, 'REQUEST HEADER', '*' * 20)
    for key, value in request.headers.items():
        print(f"{key}: {value}")
    print('*' * 20, 'REQUEST HEADER', '*' * 20, '\n')

    # 响应体
    html = """
    <html>
        <body style="text-align: center;">
            <h1>EXPLORE</h1>
            <h1>REQUEST</h1>
            <h1>HEADER</h1>
        </body>
    </html>
    """

    return HttpResponse(html)


def play_request_files(request):
    """
    获取客户端上传的文件：利用request.FILES，但仅限于post请求方法
    1. 可以接受一个或者多个文件
    2. 可以使用Python的基础知识将文件保存到硬盘
        首先打开要保存的文件
        然后读取内存中上传文件的内容写入到相应的位置
    """

    # TODO request.FILES 也是一个类似于字典的数据结构
    print(type(request.FILES))
    print(request.FILES)

    # 遍历 request.FILES
    if request.FILES:
        for key, value in request.FILES.items():
            print(f"key_type: {type(key)}")
            print(f"key: {key}")
            print(f"value_type: {type(value)}")
            print(f"value: {value}")

    # 响应体
    html = """
    <html>
        <body style="text-align: center;">
            <h1>ACQUIRE</h1>
            <h1>UPLOADING</h1>
            <h1>FILES</h1>
        </body>
    </html>
    """

    return HttpResponse(html)


def return_html(request):
    """
    响应体的内容是html
    """

    # 响应体
    content = """
    <html>
        <body style="text-align: center;">
            <h1>HttpResponse: html</h1>
        </body>
    </html>
    """

    # 响应头
    headers = {"token": 10086, "name": "guanjie sun"}

    # 响应
    http_response = HttpResponse(content=content,
                                 content_type='text/html',
                                 status=201,
                                 headers=headers)

    return http_response


def return_json(request):
    """
    响应体的内容是json
    """

    # 响应体
    data = {
        "name": "Guanjie Sun",
        "id": "221110701116",
        "age": 30,
        "hobbies": ["movies", "basketball", "pingpong"]
    }

    json_data = json.dumps(data)

    # 响应头
    headers = {"token": 10086, "name": "Lebron James"}

    # 响应
    http_response = HttpResponse(content=json_data,
                                 content_type='application/json',
                                 status=201,
                                 headers=headers)

    return http_response


def return_another_json(request):
    """
    响应体的内容是json，使用的是 JsonResponse 而不是 HttpResponse
    """

    # 响应体
    data = {
        "name": "Michael",
        "id": "123454321",
        "age": 55,
        "hobbies": ["basketball", "baseball"]
    }

    # 响应头
    headers = {"token": 88888, "sex": "male"}

    # 响应
    json_response = JsonResponse(data=data,
                                 headers=headers,
                                 content_type="text/json",
                                 status=201)

    return json_response


def return_picture(request):
    """
    响应体的内容是json
    """

    # 响应体
    path = Path(__file__).parent / "resources/dog.png"
    with open(path, 'rb') as file:
        img = file.read()

    # 响应
    http_response = HttpResponse(content=img,
                                 content_type='image/png')

    return http_response


def return_zip(request):
    """
    响应体的内容是 zip 压缩文件
    """

    # 响应体
    path = Path(__file__).parent / "resources/dog.zip"
    with open(path, 'rb') as file:
        zip_file = file.read()

    # 响应
    http_response = HttpResponse(content=zip_file,
                                 content_type='application/zip')

    return http_response


def return_mp4(request):
    """
    响应体的内容是 mp4 视频
    """

    # 响应体
    path = Path(__file__).parent / "resources/girl-crush-bomi-powerful-stage.mp4"
    with open(path, 'rb') as file:
        mp4_file = file.read()

    # 响应
    http_response = HttpResponse(content=mp4_file,
                                 content_type='video/mp4')

    return http_response


def return_mp3(request):
    """
    响应体的内容是 mp3
    """

    # 响应体
    path = Path(__file__).parent / "resources/because_of_love.mp3"
    with open(path, 'rb') as file:
        mp3_file = file.read()

    # 响应
    http_response = HttpResponse(content=mp3_file,
                                 content_type='audio/mpeg')

    return http_response


def return_gif(request):
    """
    响应体的内容是 gif
    """

    # 响应体
    path = Path(__file__).parent / "resources/dog.gif"
    with open(path, 'rb') as file:
        gif_file = file.read()

    # 响应
    http_response = HttpResponse(content=gif_file,
                                 content_type='image/gif')

    return http_response


def redirect_outside(request):
    """
    redirect to outside the project
    """

    # 响应
    http_response_redirect = HttpResponseRedirect("https://www.zhihu.com/")

    return http_response_redirect


def redirect_inside(request):
    """
    redirect to inside the project
    """

    # url = reverse("home_ns:gif_v")     # namespace:view_name
    url = reverse("goods_ns:index_v")  # namespace:view_name
    # url = reverse("project_homepage")  # view_name, "project_homepage" is the alias name of ""
    return redirect(url)

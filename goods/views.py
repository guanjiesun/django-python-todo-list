from django.http import HttpResponse


def index(request):

    # print client's IP address
    print('+' * 20, 'Client IP Address', '+' * 20)
    print("Client IP address:", request.META.get('REMOTE_ADDR'))
    print('+' * 20, 'Client IP Address', '+' * 20, '\n')

    # print request line
    print('*' * 20, 'Request Line', '*' * 20)
    print("Method:", request.method)
    print("Path:", request.path)
    print("Full URL:", request.build_absolute_uri())
    print('*' * 20, 'Request Line', '*' * 20, '\n')

    # print request headers
    print('#' * 50, 'Request Headers', '#' * 50)
    for key, value in request.headers.items():
        print(f"{key}: {value}")
    print('#' * 50, 'Request Headers', '#' * 50, '\n')

    # print request body
    print('@' * 20, 'Request Body', '@' * 20)
    if request.body.decode("utf-8") == '':
        print("request.body is empty!")
    else:
        print(request.body.decode("utf-8"))
    print('@' * 20, 'Request Body', '@' * 20, '\n')

    return HttpResponse("<h1>Message from goods->views->index</h1>")


def hello(request):
    return HttpResponse("<h1>Message from goods->views->hello</h1>")

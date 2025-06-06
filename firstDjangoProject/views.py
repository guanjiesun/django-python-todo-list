from django.http import HttpResponse


def index(request):
    # 整个项目的主页
    content = """
    <h1 style="text-align: center;">WELCOME TO MY HOMEPAGE</h1>"""

    return HttpResponse(content)

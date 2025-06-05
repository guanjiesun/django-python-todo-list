from django.http import HttpResponse


def homepage(request):
    html = """
    <html>
        <head>
            <title>HOMEPAGE</title>
        </head>
        <body style="text-align: center;">
            <h1>WELCOME TO THE HOMEPAGE OF THE WHOLE PROJECT</h1>
        </body>
    </html>
    """
    return HttpResponse(html)

from django.http import HttpResponse


def hello(request):
    html = """
    <html>
        <body style="text-align: center;">
            <h1>WELCOME TO MY HOMEPAGE!</h1>
            <h1>Hello, world!</h1>
            <h1>World, hello!</h1>
            <h1>My name is Guanjie Sun!</h1>
            <h1>My favorite programming languages:</h1>
            <ul style="list-style-position: inside; display: inline-block; text-align: left;">
                <li>Python</li>
                <li>Go</li>
                <li>C++</li>
                <li>JavaScript</li>
                <li>SQL</li>
            </ul>
            <h1>Good Good Study, Day Day Up!</h1>
        </body>
    </html>
    """
    return HttpResponse(html)

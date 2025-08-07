from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.db import transaction
from .models import TodoItem
from .forms import TodoItemForm

import json


def index(request):
    """
    - GET  请求: 显示所有 todo items
    - POST 请求: 添加一个新的 todo item. 然后重定向, 发起一次新的 GET 请求 (POST/REDIRECT/GET 模式, 避免重复的 POST 请求)
    - 其他请求：返回 HTTP 405 Method Not Allowed 错误
    """
    if request.method == 'POST':
        item_text = request.POST.get('item')
        if item_text:
            # 防止 空字符串 或者 None 插入到数据库
            TodoItem.objects.create(item=item_text)
        # redirect 函数会生成一个 HTTP 302 重定向响应, 是实现 POST/Redirect/GET 模式的核心
        # 浏览器收到这个响应后，会自动发起一个新的 GET 请求到相应的 URL
        # 需要了解 HTTP 重定向的工作原理, 可以利用 wireshark 观察详细信息
        return redirect('todo:index')
    elif request.method == 'GET':
        items = TodoItem.objects.all().order_by('id')
        # render 函数拿到数据然后渲染模板，产生 HTML 响应
        # 第一个参数是 request 对象，第二个参数是模板文件路径，第三个参数是一个字典，包含要传递给模板的数据
        # 公式: template + data -> web page(HTML)
        return render(request, 'todo/index.html', {'items': items})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def todo_item(request, item_id):
    """
    - PUT 请求: 更新一个 todo item 的内容
    - DELETE 请求: 删除一个 todo item
    - GET 请求: 显示一个 todo item 的详情
    - 其他请求：返回 HTTP 405 Method Not Allowed 错误
    """

    # 若数据库中没有主键为 item_id 的 TodoItem 对象, 立即返回一个 HTTP 404 错误响应
    item = get_object_or_404(TodoItem, pk=item_id)
    if request.method == 'GET':
        return render(request, 'todo/detail.html', {'item': item})
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        item.item = data.get('item', item.item)
        item.completed = data.get('completed', item.completed)
        item.save()

        # 返回 JSON 响应，包含更新时间
        return JsonResponse({
            'success': True,
            'updated_at': item.updated_at.strftime('%m-%d %H:%M')
        })
    elif request.method == 'DELETE':
        with transaction.atomic():  # 确保删除操作的原子性
            item.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])


def set_session(request):
    """
    设置用户的 session 数据
    """

    # 1. Django 的 SessionMiddleware 中间件 会根据 HTTP 请求头中的 Cookie 字段 来判断用户是否已经拥有 sessionid
    # 如果有, SessionMiddleware 会从数据库中django_session 表中查询该 session ID 对应的 session 数据

    # 2. 如果客户端没有携带名为 sessionid 的 Cookie, 只要视图中对 request.session 进行了写操作(如设置某个键值).
    # Django 就会自动创建一个新的 session ID, 并在响应中通过 Set-Cookie 字段将 sessionid 发送给客户端,
    # 同时将会话数据保存到服务器端(如数据库、缓存等 session 后端).

    # 3. 客户端在后续请求中会自动携带该 session ID, 从而实现会话保持.

    request.session['username'] = 'Guanjie Sun'
    request.session['email'] = 'guanjie.sun@outlook.com'
    return HttpResponse('Session set successfully!')


def get_session(request):
    """
    获取 session 数据
    如果客户端没有携带 session ID 或者是无效的 session ID, 那么 request.session 将是一个空字典
    如果客户端携带了有效的 session ID, 那么 request.session 将包含之前设置的 'username' 和 'email' 数据发送给客户端
    """
    username = request.session.get('username', 'Guest')
    email = request.session.get('email', 'No email set')
    return HttpResponse(f'Hello, {username}@{email}!')


def add_todo_item(request):
    """ 利用 Django 的表单系统来添加 todo item """
    if request.method == 'POST':
        # 浏览器的刷新（F5）行为 或 点击地址栏再按回车 是“重新发送上一次的请求”
            # 也就是说：
            # 如果这个页面是通过 GET 请求获得的 → 刷新会重新发 GET；
            # 如果这个页面是通过 POST 请求获得的（例如你刚提交了表单）→ 刷新会尝试重新发 POST！
        # 所以如果用户在添加待办事项后刷新页面，浏览器会重新发送 POST 请求
        # 这会导致重复添加同一个待办事项
        # 为了避免这种情况，可以在处理 POST 请求后重定向到 GET 请求
        # 这样浏览器就会发起新的 GET 请求，而不是重新发送 POST 请求
        # 这就是所谓的 POST/Redirect/GET 模式
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect 函数会生成一个 HTTP 302 重定向响应
            # 浏览器收到这个响应后，会自动发起一个新的 GET 请求到相应的 URL
            # 302 的作用就是“Post → Redirect → Get” 模式的核心
            return redirect('todo:add_todo_item')
    else:
        form = TodoItemForm()
    return render(request, 'todo/add_todo_item.html', {'form': form})

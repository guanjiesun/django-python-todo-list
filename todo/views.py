from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.db import transaction
from .models import TodoItem

import json


def index(request):
    """
    显示所有 items
    - GET 请求：返回 item 列表页面
    - POST 请求：创建新 item 然后重定向，发起一次新的 GET 请求 (POST -> redirect -> GET)
    - 其他请求：返回 405 不允许
    """
    if request.method == 'POST':
        item_text = request.POST.get('item')
        if item_text:
            # 防止 空字符串 或者 None 插入到数据库
            TodoItem.objects.create(item=item_text)
        # post->redirect->get
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
    查询、修改和删除一个 item
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

    1. Django 的 SessionMiddleware 中间件 会根据 HTTP 请求头中的 Cookie 字段 来判断用户是否已经拥有 sessionid
    如果有, SessionMiddleware 会从数据库中django_session 表中查询该 session ID 对应的 session 数据

    2. 如果客户端没有携带名为 sessionid 的 Cookie, 只要视图中对 request.session 进行了写操作(如设置某个键值).
    Django 就会自动创建一个新的 session ID, 并在响应中通过 Set-Cookie 字段将 sessionid 发送给客户端, 
    同时将会话数据保存到服务器端(如数据库、缓存等 session 后端).

    3. 客户端在后续请求中会自动携带该 session ID, 从而实现会话保持.
    """

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

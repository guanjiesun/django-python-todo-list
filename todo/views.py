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
        return HttpResponse(status=204)
    elif request.method == 'DELETE':
        with transaction.atomic():  # 确保删除操作的原子性
            item.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

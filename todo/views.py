from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.db import transaction
from .models import TodoItem

import json


def index(request):
    """
    显示所有 items：
    - GET 请求：返回 item 列表页面
    - POST 请求：创建新 item 然后返回 item 列表页面
    - 其他请求：返回 405 不允许
    """
    if request.method in ['POST', 'GET']:
        if request.method == 'POST':
            item_text = request.POST.get('item')
            if item_text:
                # 防止 空字符串 或者 None 插入到数据库
                TodoItem.objects.create(item=item_text)
        items = TodoItem.objects.all().order_by('id')
        return render(request, 'todo/index.html', {'items': items})
    else:
        # HttpResponseNotAllowed(['GET', 'POST']) 会返回一个 405 状态码，告诉前端“方法不允许”
        return HttpResponseNotAllowed(['GET', 'POST'])


def todo_item(request, item_id):
    """
    查询、修改和删除一个 item
    """
    item = get_object_or_404(TodoItem, pk=item_id)
    if request.method == 'GET':
        return render(request, 'todo/detail.html', {'item': item})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        item.item = data.get('item', item.item)
        item.completed = data.get('completed', item.completed)
        item.save()
        return redirect('todo:index')  # namespace:url_name
    elif request.method == 'DELETE':
        with transaction.atomic():  # 确保删除操作的原子性
            item.delete()
        return redirect('todo:index')  # namespace:url_name
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import TodoItem


def index(request):
    # 向用户展示所有的 items
    items = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'items': items})


def add(request):
    """ 添加一个新的 item
    1. 将用户提交的item保存到数据库中
    2. 然后重定向到主页
    """
    if request.method == 'POST':
        item_text = request.POST.get('item')
        if item_text:
            TodoItem.objects.create(item=item_text)

    # 根据 namespace:url_name 反向解析出对应的url
    url = reverse("todo:index")
    return redirect(url)

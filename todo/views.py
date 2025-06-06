from django.shortcuts import render, redirect
from django.urls import reverse
from .models import TodoItem


def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'items': items})


def add_todo(request):
    if request.method == 'POST':
        item_text = request.POST.get('item')
        if item_text:
            TodoItem.objects.create(item=item_text)

    # 根据 namespace:url_name 反向解析出对应的url
    url = reverse("todo:todo_list")
    return redirect(url)

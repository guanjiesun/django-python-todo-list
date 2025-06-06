from django.shortcuts import render, redirect
from .models import TodoItem


def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'items': items})


def add_todo(request):
    if request.method == 'POST':
        item_text = request.POST.get('item')
        if item_text:
            TodoItem.objects.create(item=item_text)
    return redirect('todo_list')

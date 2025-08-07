from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.todo_item, name='todo_item'),
    path('set-session/', views.set_session, name='set_session'),
    path('get-session/', views.get_session, name='get_session'),
    path('add-todo-item/', views.add_todo_item, name='add_todo_item'),
]

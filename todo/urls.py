from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.todo_item, name='todo_item'),
]

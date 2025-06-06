from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # TODO name 是为每个 URL 路由起一个唯一的名字，用于反向解析 URL（即通过名字生成 URL 地址），不必硬编码 URL 路径
    path('', views.index, name='index'),

    # TODO include 是 Django 提供的一个函数，用来引入其他模块的 URL 配置
    # goods.urls 表示导入 goods 这个 package 的 urls 模块(urls.py)
    # freight/ 表示给所有 goods 相关的 URL 加一个统一的前缀 freight/
    # namespace 是 URL 名称的命名空间，它是 Django 为了解决多 app 中 URL 名字冲突、方便反向解析设置的机制
    # namespace 机制需要 app_name 支持，每一个应用的 urls.py 中要定义 app_name 变量, app_name 的值是任意的
    path('freight/', include('goods.urls', namespace='goods_ns')),
    path('house/', include('home.urls', namespace='home_ns')),
    path('cracker/', include("cookies.urls", namespace='cookies_ns')),
    path('todo/', include('todo.urls', namespace='todo'))
]

from django.urls import path

from . import views

""" 为什么在 urls.py 文件中设置 app_name
1. app_name 本身不会直接在代码中使用， 而是 Django 用 app_name 配合 namespace 来组织
URL 反向解析（如 {% url %} 或 reverse()）时使用的
2. app_name 用于 Django 识别 app 的 URL 名字空间
"""
app_name = 'app_name_of_goods'

urlpatterns = [
    # TODO name 是为每个 URL 路由起一个唯一的名字，用于反向解析 URL（即通过名字生成 URL 地址），不必硬编码 URL 路径
    path('index/', views.index, name='index_v'),
    path('hello/', views.hello, name='hello_v'),
]

from django.urls import path

from . import views

app_name = 'app_name_of_cookies'

urlpatterns = [
    # TODO name 是为每个 URL 路由起一个唯一的名字，用于反向解析 URL（即通过名字生成 URL 地址），不必硬编码 URL 路径
    path('set/', views.set_cookie, name='s_cookie'),
    path('get/', views.get_cookie, name='g_cookie'),
    path('delete/', views.delete_cookie, name='d_cookie'),
]

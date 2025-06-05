from django.urls import path

from . import views

""" 为什么在 urls.py 文件中设置 app_name
1. app_name 本身不会直接在代码中使用， 而是 Django 用 app_name 配合 namespace 来组织
URL 反向解析（如 {% url %} 或 reverse()）时使用的
2. app_name 用于 Django 识别 app 的 URL 名字空间
"""
app_name = 'app_name_of_home'

urlpatterns = [
    path('index/', views.index),
    path('query/', views.save_query_params_2json),
    path('body/', views.obtain_request_body),
    path('header/', views.explore_request_headers),
    path('files/', views.play_request_files),
    path('return-html/', views.return_html),
    path('return-json/', views.return_json),
    path('return-another-json/', views.return_another_json),
    path('return-picture/', views.return_picture),
    path('return-zip/', views.return_zip),
    path('return-mp4/', views.return_mp4),
    path('return-mp3/', views.return_mp3),
    # TODO name 是为每个 URL 路由起一个唯一的名字，用于反向解析 URL（即通过名字生成 URL 地址），不必硬编码 URL 路径
    path('return-gif/', views.return_gif, name='gif_v'),  # name is an alias of 'return-gif'
    path('redirect-outside/', views.redirect_outside),
    path('redirect-inside/', views.redirect_inside),
]

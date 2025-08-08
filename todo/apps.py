from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # 指定这个 todo app 中的模型的主键字段默认使用的类型
    name = 'todo'

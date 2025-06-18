from django.db import models


class TodoItem(models.Model):
    item = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    # auto_now_add 设置为 True, 则在调用 .create() 创建对象时会自动设置 created_at 字段的值为当前时间
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # auto_now 设置为 True, 则每次调用 .save() 的时候都会更新 updated_at 字段的值为当前时间
    # .create() 内部会调用 .save(), 所以在创建对象时 updated_at 字段也会被设置为当前时间
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        # 返回待办事项的内容作为字符串表示
        return self.item

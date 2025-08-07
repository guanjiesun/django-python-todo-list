from django import forms
from .models import TodoItem


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem   # 表单是基于 TodoItem 模型的
        fields = ['item']  # 声明只用模型里的 item 字段作为表单字段 

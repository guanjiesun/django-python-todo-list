from django.db import models


class TodoItem(models.Model):
    item = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item

from django.db import models
from django.utils import timezone
from .user import User


class Comment(models.Model):
    comment_autohor = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_creation_date = models.DateTimeField()
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.comment_autohor

from django.db import models
from django.utils import timezone
import uuid
from .user import User


class Comment(models.Model):
    autohor = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    text = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f'{self.comment_autohor}'

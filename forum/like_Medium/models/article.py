from django.db import models
import uuid
from .user import User


class Article(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    creation_date = models.DateTimeField()
    rating = models.BooleanField(null=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f'{self.article_title} from {self.article_creator}'

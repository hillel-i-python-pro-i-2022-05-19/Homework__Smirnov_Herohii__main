from django.db import models
import uuid
from .user import User


class Article(models.Model):
    article_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=50)
    article_text = models.TextField()
    article_creation_date = models.DateTimeField()
    article_rating = models.BooleanField(null=True)
    article_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f'{self.article_title} from {self.article_creator}'

from django.db import models
import uuid

class User(models.Model):
    user_nickname = models.CharField(max_length=20)
    user_creation_date = models.DateTimeField()
    user_rating = models.PositiveSmallIntegerField(null=True, blank=True)
    user_articles_number = models.IntegerField(null=True,blank=True)
    user_comments_number = models.IntegerField(null=True, blank=True)
    user_avatar = models.ImageField(null=True, blank=True)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.user_nickname

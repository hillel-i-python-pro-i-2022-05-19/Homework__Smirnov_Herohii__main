from django.utils import timezone

"""
Some methonds for Article model to add after
"""

def latest_article(self):
    if (self.creation_date - timezone.datetime) <=7:
        return f'{self.article.title}'

def article_info(self):
    return f'Title: {self.title}, creator {self.creator}, time{self.creation_date}'


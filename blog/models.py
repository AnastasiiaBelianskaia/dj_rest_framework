from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200, default='Without title')
    text = models.TextField()
    pubdate = models.DateTimeField('date published', auto_now=True)

    class Meta:
        ordering = ['pubdate']

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pubdate = models.DateTimeField('date published', auto_now=True)

    class Meta:
        ordering = ['pubdate']

    def __str__(self):
        return self.text

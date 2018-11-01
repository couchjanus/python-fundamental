# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

# Post models here.
class Post(models.Model):

    creator = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True,
    )

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def to_dict(self, user):
        return {
            'id': self.id,
            'title': self.title,
            'how_long_ago': datetime.isoformat(self.pub_date),
            'creator': self.creator.username,
        }

    def __str__(self):
        return self.title

# PostStatistic models here.

class PostStatistic(models.Model):

    post = models.ForeignKey(Post, on_delete=models.PROTECT)           # внешний ключ на статью
    view_date = models.DateField(default=timezone.now)   # дата
    views = models.IntegerField(default=0)   # количество просмотров в эту дату

    def __str__(self):
        return self.post.title


class Comment(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
    )
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('Comment', related_name='replies', on_delete=models.CASCADE, null=True, default=None, blank=True)
    content = models.TextField(null=True)

    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.content


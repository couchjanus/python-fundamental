# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Post models here.
class Post(models.Model):

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.title

# PostStatistic models here.

class PostStatistic(models.Model):

    post = models.ForeignKey(Post, on_delete=models.PROTECT)           # внешний ключ на статью
    view_date = models.DateField(default=timezone.now)   # дата
    views = models.IntegerField(default=0)   # количество просмотров в эту дату

    def __str__(self):
        return self.post.title

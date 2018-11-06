# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from taggit.managers import TaggableManager

from taggit.models import Tag

class Category(models.Model):
    """
    Model representing a category.
    """
    name = models.CharField(max_length=200, help_text="Enter a category")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


# Post models here.
class Post(models.Model):

    creator = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True,
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique = True, default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    picture = models.ImageField(upload_to='blog/%Y/%m/%d', default='default.png')
    tags = TaggableManager()
    updated_date = models.DateField(blank=True, null=True)
    category = models.ManyToManyField(Category, help_text="Select a category for this post")
    # ManyToManyField used because category can contain many posts. Posts can cover many categories.

    POST_STATUS = (
        ('d', 'Draft'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=POST_STATUS, blank=True, default='d', help_text='Post availability')

    
    def to_dict(self, user):
        return {
            'id': self.id,
            'title': self.title,
            'how_long_ago': datetime.isoformat(self.pub_date),
            'creator': self.creator.username,
        }

    # def get_tag_names(self):
    #     return [tag.name for tag in Tag.objects.get_for_object(self)]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular post instance.
        """
        return reverse('post_detail', args=[str(self.id)])

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


# -*- coding: utf-8 -*-

from django import template
from django.db.models import Sum
from django.utils import timezone
from django.db.models import Count

from django.utils.safestring import mark_safe
import markdown

from blog.models import Post



register = template.Library()

# Пример простого тега

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/recent_posts.html')   
def get_recent_posts_for_week(count=5):

    recent = Post.objects.filter(
        # отфильтровываем записи за последние 7 дней
        pub_date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
    ).values(
        # Забираем интересующие нас поля, а именно id и заголовок
        'id', 'title',
    ).order_by(
        # отсортируем записи по убыванию
        '-pub_date')[:count]    # Заберём последние :count записей

    return {'recent': recent}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

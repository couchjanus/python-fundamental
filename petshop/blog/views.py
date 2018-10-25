from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Sum

from .models import Post, PostStatistic

def index(request):
    """
    View function for home page of site.
    """
    posts=Post.objects.all()

    return render(
        request,
        'blog/index.html',
        context={'posts':posts},
    )

def view(request, id):
    post = get_object_or_404(Post, id=id)

    obj, created = PostStatistic.objects.get_or_create(
        defaults={
            "post": post,
            "view_date": timezone.now()
        },
        view_date=timezone.now(), post=post    
    )
    # инкрементируем счётчик просмотров 
    # и обновляем поле в базе данных

    obj.views += 1
    obj.save(update_fields=['views'])

    return render(
        request,
        'blog/blog_post.html',
        context={'post':post}
        )
# забираем список 5 последний самых популярных статей за неделю
def get_popular(request):
    # отфильтровываем записи за последние 7 дней
    popular = PostStatistic.objects.filter(
        view_date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
    ).values(
        # Забираем интересующие нас поля, а именно id и заголовок
        'id', 'post_id', 'post__title'
    ).annotate(
        # Суммируем записи по просмотрам
        views=Sum('views')
    ).order_by(
        '-views')[:5]
    return render(request, 'blog/posts.html', context={'popular_list':popular},)
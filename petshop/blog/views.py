from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Sum
import json
from django.views.generic import ListView, CreateView

from django.views.generic import DetailView
from django.contrib.auth.models import User
from .models import Post, PostStatistic

from .forms import CommentForm

from taggit.models import Tag

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class PostListView(ListView):
    # template_name = 'blog/index.html'
    # model = Post
    # paginate_by = '10'
    queryset = Post.objects.order_by('-pub_date')

class TagIndexView(TagMixin, ListView):
    template_name = 'blog/index.html'
    model = Post
    paginate_by = '10'
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


class AuthorDetail(DetailView):
    
    model = User

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the posts
        context['post_list'] = Post.objects.all()
        return context

class JanusPostList(ListView):
    
    context_object_name = 'post_list'
    queryset = Post.objects.filter(creator__username='janus')
    template_name = 'blog/janus_list.html'

class PostDetailView(DetailView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

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

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.creator = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

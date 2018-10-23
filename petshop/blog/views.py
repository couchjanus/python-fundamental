from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    """
    View function for home page of site.
    """

    # posts=Post.objects.all().count()
    posts=Post.objects.all()

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'blog/index.html',
        context={'posts':posts},
    )

def view(request, id):
    post = get_object_or_404(Post, id=id)

    return render(
        request,
        'blog/blog_post.html',
        context={'post':post}
        )

from django.shortcuts import render

from .models import Category
# Create your views here.
def index(request):
    """
    View function for home page of site.
    """


    # количество categories
    count_categories=Category.objects.all().count()

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'title':'Hello Products', 'count_categories':count_categories},
    )

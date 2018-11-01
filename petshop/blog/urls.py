from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PostListView.as_view(), name='list'),
    url(r'(?P<pk>[-\d]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    path('popular/', views.get_popular, name='get_popular'),
    url(r'(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

    # path('<int:id>/', views.view, name='post_detail'),  
]

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('popular/', views.get_popular, name='get_popular'),
    path('<int:id>/', views.view, name='post_detail'),  
]

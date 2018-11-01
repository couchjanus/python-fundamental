"""petshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.contrib.auth import views as core_views
from site_auth import views as auth_views

from django.views.generic import TemplateView

from site_auth.forms import LoginForm

from pages.views import HomePageView, AboutPageView

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^signup/$', auth_views.signup, name='signup'),
    url(r'^home/$', auth_views.home, name='home'),
    url(r'^login/$', core_views.LoginView.as_view(template_name='login.html', authentication_form = LoginForm), name='login'),  
    url(r'^logout/$', core_views.LogoutView.as_view(next_page='login'), name='logout'),

    # path('', include('pages.urls')),

    url(r'^about/', TemplateView.as_view(template_name="about.html")),

    # url(r'^about/', AboutPageView.as_view()),
    # url(r'^$', HomePageView.as_view()),

    url(r'^products/', include('products.urls')),
    url(r'^blog/', include('blog.urls')),
]



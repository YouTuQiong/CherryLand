"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from blog import views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index.html', views.index),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^Article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^Archives/', views.archives, name='archives'),
    url(r'^Archive.html', views.archives, name='archives'),
    url(r'^Category/(?P<pk>[0-9]+)/$', views.Category, name='Category'),
    url(r'^Tag/(?P<pk>[0-9]+)/$', views.Tag, name='Tag'),
    url(r'^about.html', views.about, name='about'),
    url(r'^about', views.about, name='about'),
    url(r'^reader', views.reader, name='reader'),
    url(r'^reader.html', views.reader, name='reader'),
    url(r'^mygays', views.mygays, name='mygays'),
    url(r'^mygays.html', views.mygays, name='mygays'),

]

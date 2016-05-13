from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /blog/5/
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]

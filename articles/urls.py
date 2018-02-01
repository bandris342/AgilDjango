from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.articles_list, name='articles_list'),
    url(r'^detail/(?P<pk>\d+)$', views.article_detail, name='article_detail'),
    url(r'^edit/(?P<pk>\d+)$', views.article_edit, name='article_edit'),
    url(r'^new/$', views.article_new, name='article_new'),
    url(r'^delete/(?P<pk>\d+)$', views.article_delete, name='article_delete'),
]
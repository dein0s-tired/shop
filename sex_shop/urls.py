from django.conf.urls import patterns, url

from sex_shop import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^categories/$', views.categories, name='categories'),
                       url(r'^categories/(?P<category_id>\d+)/$', views.category, name='category')
                       )

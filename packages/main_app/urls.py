from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    
    #url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)', views.each_post, name='each_post')
    url(r'^(?P<slug>[\w-]+)/$', views.each_post, name='each_post')
    
]
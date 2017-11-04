from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^$', views.home, name='home'),
    
    url(r'^edit/(?P<pk>[\d]+)/$', views.edit_post, name='edit_post'),
    
]
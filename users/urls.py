from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
 	url(r'^$',views.users.as_view(), name='users'),
 	url(r'^new/$', views.users_new, name='user_new'),
 	url(r'^delete/@(?P<pk>\d+)/$', views.user_delete.as_view(), name='user_delete'),
 	url(r'^suspend/@(?P<pk>\d+)/$', views.user_suspend, name='user_suspend'),
]
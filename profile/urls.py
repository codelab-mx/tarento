from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
 	url(r'^(?P<pk>\d+)/$', views.profile.as_view(), name='profile'),
 	#url(r'^new/$', views.users_new.as_view(), name='user_new'),
 	#url(r'^@(?P<user_name>[-\w.]+)/$', views.app_users_view, name='users_view')
]
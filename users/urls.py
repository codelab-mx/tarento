from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
 	url(r'^$',views.users.as_view(), name='users'),
 	url(r'^new/$', views.app_users_new, name='users_new'),
 	url(r'^@(?P<user_name>[-\w.]+)/$', views.app_users_view, name='users_view'),
 	url(r'^contracts/$', views.app_users_contracts, name='users_contracts'),
 	url(r'^contracts/view$', views.app_users_contracts_view, name='users_contracts_view'),
 	url(r'^contracts/new$', views.app_users_contracts_new, name='users_contracts_new'),
]
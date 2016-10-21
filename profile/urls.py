from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
 	url(r'^@(?P<pk>\d+)/$', views.profile, name='profile'),


 	url(r'^edit/@(?P<pk>\d+)/$', views.edit_profile, name='edit_profile'),
 	url(r'^edit/data/@(?P<pk>\d+)/$', views.edit_data_profile, name='edit_data_profile'),
 	url(r'^edit/contact/@(?P<pk>\d+)/$', views.edit_contact_profile, name='edit_contact_profile'),
 	url(r'^edit/hiring/@(?P<pk>\d+)/$', views.edit_hiring_profile, name='edit_hiring_profile'),
 	url(r'^contracts/$', views.contracts.as_view(), name='contracts'),
 	url(r'^contracts/new/$', views.new_contract, name='new_contract'),
 	url(r'^contracts/edit/@(?P<pk>\d+)/$', views.edit_contract, name='edit_contract'),
 	url(r'^contract/@(?P<pk>\d+)/$', views.contract, name='contract'),
]
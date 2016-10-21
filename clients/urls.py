"""nexus/clients URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^clients/', include('clients.urls')),
    url(r'^calendar/@(?P<pk>\d+)/$', views.calendar, name='calendar'),
    url(r'^edit/@(?P<pk>\d+)/$', views.edit_client, name='edit_client'),
    url(r'^delete/@(?P<pk>\d+)/$', views.delete_client.as_view(), name='delete_client'),
    url(r'^$', views.list_clients.as_view(), name='clients_dashboard'),
    url(r'^new/$', views.new_clients, name='add_new_client'),
    url(r'^profile/@(?P<pk>\d+)$', views.profile_clients, name='profile_client'),
]


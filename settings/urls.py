from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^$', views.home, name='home'),
 	url(r'^login/$', views.login_crm, name='login'),
 	url(r'^logout/$', views.logout_crm, name='logout'),
 	url(r'^users/', include('users.urls')),
 	url(r'^profile/', include('profile.urls')),
	#url(r'^admin/', admin.site.urls),
]

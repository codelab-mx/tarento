# -*- coding: utf-8
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import Template
from . import forms
from . import models

# Class based views
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

##########################
#  Render all the Users  #
##########################
@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('auth.add_user', login_url='home'), name='dispatch')
class users(ListView):
    model = User
    paginate_by = 10
    template_name = 'users/index.html'
    def get_queryset(self, *args, **kwargs):
    	qs = super(users, self).get_queryset(*args, **kwargs).exclude(is_superuser=1)
    	return qs
    def get_context_data(self, *args, **kwargs):
    	context = super(users, self).get_context_data(*args, **kwargs)
    	context["title"] = "Empleados"
    	context["subtitle"] = "Usuarios registrados en el sistema"
    	context["page"] = "Tabla de Usuarios"
    	context["btn"] = "Nuevo Empleado"
    	context["btn_url"] = reverse("user_new")
    	return context
	
#######################################
#  Register a New User in the system  #
#######################################
@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('auth.add_user', login_url='home'), name='dispatch')
class users_new(CreateView):
	form_class = forms.UserRegisterForm
	template_name = "users/forms/new.html"
	def get_context_data(self, *args, **kwargs):
		context = super(users_new, self).get_context_data(*args, **kwargs)
		context["title"] = "Nuevo Empleado"
		context["subtitle"] = "Agregar un usuario nuevo al sistema"
		context["page"] = "Formulario de registro"
		context["btn"] = "Cancelar"
		context["btn_url"] = reverse("users")
		return context
	def get_success_url(self):
		return reverse('users')

###################################
#  Delete User from the database  #
###################################
@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('auth.delete_user', login_url='home'), name='dispatch')
class user_delete(DeleteView):
	template_name = "dashboard/delete_form.html"
	model = User
	def get_success_url(self):
		return reverse("users")	
	def get_context_data(self, *args, **kwargs):
		context = super(user_delete, self).get_context_data(*args, **kwargs)
		context["title"] = "Eliminar empleado del sistema"
		context["subtitle"] = "Estás a punto de eliminar a este usuario"
		context["btn"] = "Cancelar"
		context["btn_url"] = reverse("users")
		context["page"] = "¿Estás seguro?"
		return context
	def get_queryset(self, *args, **kwargs):
		qs = super(user_delete, self).get_queryset(*args, **kwargs).exclude(is_superuser=1)
		return qs

##################
#  SUSPEND USER  #
##################
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def user_suspend(request, pk):
	btn = 'Cancelar'
	btn_url = reverse('users')
	title = 'Suspender Usuario'
	subtitle = 'El usuario no podrá hacer uso del sistema'
	user = User.objects.filter(id__exact=pk).exclude(is_superuser=1)
	if (request.POST.get('is_active')):
		status = int(request.POST.get('profile_status'))
		User.objects.filter(id=pk).update(is_active=status)
		return HttpResponseRedirect(reverse('users'))
	return render(request, 'users/forms/suspend.html', locals())
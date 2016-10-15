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
    	qs = super(users, self).get_queryset(*args, **kwargs).exclude(is_superuser=1).order_by('username')
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
@permission_required('auth.add_user', login_url='home')
@login_required(login_url='login')
def users_new(request):
	title = "Nuevo Empleado"
	subtitle = "Agregar un usuario nuevo al sistema"
	page = "Formulario de registro"
	btn = "Cancelar"
	btn_url = reverse("users")
	form = forms.UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		#user.groups.add(Group.objects.get(name=grupo))
		return HttpResponseRedirect(reverse('users'))
	return render(request, 'users/forms/new.html', locals())

###################################
#  Delete User from the database  #
###################################
@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('auth.delete_user', login_url='home'), name='dispatch')
class user_delete(DeleteView):
	template_name = "users/forms/delete.html"
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
	object = get_object_or_404(User.objects.exclude(is_superuser=1), id=pk)
	if object.is_active == True:
		title = 'Suspender Usuario'
		page = 'no podrá hacer uso del sistema'
		subtitle = 'El usuario no podrá acceder al portal'
		btn_sus = 'Suspender'
		status = 0
		bg = 'ff902b'
	else:
		title = 'Habilitar usuario'
		page = 'podrá hacer uso del sistema'
		subtitle = 'Permitir el acceso al usuario al portal'
		btn_sus = 'Habilitar'
		status = 1
		bg = '3483e7'
	if (request.POST.get('confirm')):
		User.objects.filter(id=pk).update(is_active=status)
		return HttpResponseRedirect(reverse('users'))
	return render(request, 'users/forms/suspend.html', locals())
# -*- coding: utf-8
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import Template
from . import forms
from . import models
###################
#   Users Logic   #
###################

#Render all the users 
@permission_required('auth.add_user', login_url='dashboard')
@login_required(login_url='login')
def app_users(request):
	title = 'Empleados'
	subtitle = 'Usuarios registrados en el sistema'
	page = 'Tabla de Usuarios'
	btn = 'Nuevo Empleado'
	btn_url = reverse('users_new')
	groups = Group.objects.all()
	p_list = User.objects.exclude(is_superuser=1).all()
	paginator = Paginator(p_list, 10)
	p = request.GET.get('p')
	try:
		lists = paginator.page(p)
	except PageNotAnInteger:
		lists = paginator.page(1)
	except EmptyPage:
		lists = paginator.page(paginator.num_pages)
	return render(request, 'users/index.html', locals())

	
# Register User Form,
@permission_required('auth.add_user', login_url='dashboard')
@login_required (login_url='login')
def app_users_new(request):
	title = 'Nuevo Empleado'
	subtitle = 'Agregar un usuario nuevo al sistema'
	page = 'Formulario de registro'
	btn = 'Cancelar'
	btn_url = reverse('users')
	form = forms.UserRegisterForm(request.POST or None)
	profile_form = models.ProfileForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		f = profile_form.save(commit=False)
		f.save()
		user.save()
		#user.groups.add(Group.objects.get(name=grupo))
		return HttpResponseRedirect(reverse('users'))
	return render(request, 'dashboard/form.html', locals())

@permission_required('auth.add_user', login_url='dashboard')
@login_required (login_url='login')
def app_users_new(request):
	title = 'Nuevo Empleado'
	subtitle = 'Agregar un usuario nuevo al sistema'
	page = 'Formulario de registro'
	btn = 'Cancelar'
	btn_url = reverse('users')
	#group = Group.objects.filter(name=grupo).count()
	#if group == 1:
	form = forms.UserRegisterForm(request.POST or None)
	profile_form = models.ProfileForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		f = profile_form.save(commit=False)
		f.save()
		user.save()
		#user.groups.add(Group.objects.get(name=grupo))
		return HttpResponseRedirect(reverse('users'))
	return render(request, 'dashboard/form.html', locals())

#Render user profile
@permission_required('auth.change_user', login_url='dashboard')
@login_required (login_url='login')
def app_users_view(request, user_name):
	user = User.objects.filter(username__exact=user_name).exclude(is_superuser=1)
	return render(request, 'dashboard/form.html', locals())


#Be careful, this def delete users and all the information associate with
def app_users_delete(request, user_name):
	user = User.objects.filter(username=user_name).exclude(is_superuser=1)
	user.delete()
	return HttpResponseRedirect(reverse('usuarios'))


@login_required (login_url='login')
def app_users_contracts(request):
	title = 'Contratos'
	subtitle = 'Contratos registrados en el sistema'
	page = 'Tabla de Contratos'
	btn = 'Nuevo Contrato'
	btn_url = reverse('users_contracts_new')
	groups = Group.objects.all()
	p_list = models.Contracts.objects.all()
	paginator = Paginator(p_list, 10)
	p = request.GET.get('p')
	try:
		lists = paginator.page(p)
	except PageNotAnInteger:
		lists = paginator.page(1)
	except EmptyPage:
		lists = paginator.page(paginator.num_pages)
	return render(request, 'users/contracts.html', locals())

@login_required(login_url='login')
def app_users_contracts_new(request):
	title = 'Crear nuevo contrato'
	subtitle = 'Contratos registrados en el sistema'
	page = 'Crear contrato'
	btn = 'Cancelar'
	btn_url = reverse('users_contracts')
	form = models.ContractsForm(request.POST or None)
	if form.is_valid():
		f = form.save(commit=False)
		f.save()
		return HttpResponseRedirect(reverse('users_contracts'))
	return render(request, 'dashboard/form.html', locals())

def app_users_contracts_view(request):
	useer = 'Hola'
	title = 'Ver contrato'
	subtitle = 'Contrato'
	page = 'Ver contrato'
	btn = 'Cancelar'
	btn_url = reverse('users_contracts')
	contract = models.Contracts.objects.get(id=2)
	template = Template("My name is {{ useer }}.")
	return render(request, 'users/contracts.html', locals())

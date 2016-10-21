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

###################
#  User Profile   #
###################
@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('auth.add_user', login_url='home'), name='dispatch')
class profile(DetailView):
    model = User
    template_name = 'profile/index_profile.html'
    def get_queryset(self, *args, **kwargs):
    	qs = super(profile, self).get_queryset(*args, **kwargs).exclude(is_superuser=1)
    	return qs
    def get_context_data(self, *args, **kwargs):
    	context = super(profile, self).get_context_data(*args, **kwargs)
    	context["title"] = "Empleados"
    	context["btn"] = "Editar empleado"
    	context["btn_url"] = reverse("user_new")
    	return context
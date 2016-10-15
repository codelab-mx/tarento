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
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def profile(request, pk):
    object = get_object_or_404(User.objects.exclude(is_superuser=1), id=pk)
    title = object.username
    subtitle = 'Perfil de usuario'
    btn = 'Editar empleado'
    btn_url = reverse('edit_profile', kwargs={'pk':pk})
    return render(request, 'profile/index_profile.html', locals())

###################
#  Edit Profile   #
###################
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def edit_profile(request, pk):
    btn = 'Cancelar'
    btn_url = reverse('profile', kwargs={'pk':pk})
    object = get_object_or_404(User.objects.exclude(is_superuser=1), id=pk)
    form = forms.UserRegisterForm(request.POST or None, instance=object)
    if form.is_valid():
        update = form.save(commit=False)
        update.save()
        return HttpResponseRedirect(reverse('profile', kwargs={'pk':pk}))
    return render(request, 'dashboard/form.html', locals())

###########################
#   Edit Aditional data   #
###########################
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def edit_data_profile(request, pk):
    btn = 'Cancelar'
    btn_url = reverse('profile', kwargs={'pk':pk})
    object = get_object_or_404(User.objects.exclude(is_superuser=1), id=pk)
    profile, created = models.Profile.objects.get_or_create(user=object)
    object = get_object_or_404(models.Profile, user_id=pk)
    form = models.ProfileForm(request.POST or None, instance=object)
    if form.is_valid():
        update = form.save(commit=False)
        update.save()
        return HttpResponseRedirect(reverse('profile', kwargs={'pk':pk}))
    return render(request, 'dashboard/form.html', locals())

#########################
#   Edit Contact data   #
#########################
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def edit_contact_profile(request, pk):
    btn = 'Cancelar'
    btn_url = reverse('profile', kwargs={'pk':pk})
    object = get_object_or_404(User.objects.exclude(is_superuser=1), id=pk)
    contact, created = models.Contact.objects.get_or_create(user=object)
    object = get_object_or_404(models.Contact, user_id=pk)
    form = models.ContactForm(request.POST or None, instance=object)
    if form.is_valid():
        update = form.save(commit=False)
        update.save()
        return HttpResponseRedirect(reverse('profile', kwargs={'pk':pk}))
    return render(request, 'dashboard/form.html', locals())
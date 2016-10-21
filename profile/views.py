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
from django.contrib import messages
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
    title = 'Editar Información de Acceso'    
    btn = 'Ver Perfil'
    btn_url = reverse('profile', kwargs={'pk':pk})
    object = get_object_or_404(User.objects.exclude(is_superuser=1), id=pk)
    u = object.username
    title = 'Editar {0}'.format(u,)
    subtitle = 'Editar información personal'
    form = forms.UserRegisterForm(request.POST or None, instance=object)
    if form.is_valid():
        update = form.save(commit=False)
        update.save()
        return HttpResponseRedirect(reverse('profile', kwargs={'pk':pk}))
    return render(request, 'profile/forms/edit_user.html', locals())

###########################
#   Edit Aditional data   #
###########################
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def edit_data_profile(request, pk):
    btn = 'Ver Perfil'
    btn_url = reverse('profile', kwargs={'pk':pk})
    object = get_object_or_404(User.objects.exclude(is_superuser=1), id=pk)
    u = object.username
    title = 'Editar {0}'.format(u,)
    subtitle = 'Editar información personal'
    profile, created = models.Profile.objects.get_or_create(user=object)
    object = get_object_or_404(models.Profile, user_id=pk)
    form = forms.ProfileForm(request.POST or None, instance=object)
    if form.is_valid():
        update = form.save(commit=False)
        update.save()
        return HttpResponseRedirect(reverse('edit_data_profile', kwargs={'pk':pk}))
    return render(request, 'profile/forms/edit_user.html', locals())

#########################
#   Edit Contact data   #
#########################
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def edit_contact_profile(request, pk):
    btn = 'Ver Perfil'
    btn_url = reverse('profile', kwargs={'pk':pk})
    object = get_object_or_404(User.objects.exclude(is_superuser=1), id=pk)
    u = object.username
    title = 'Editar {0}'.format(u,)
    subtitle = 'Editar información personal'
    contact, created = models.Contact.objects.get_or_create(user=object)
    object = get_object_or_404(models.Contact, user_id=pk)
    form = forms.ContactForm(request.POST or None, instance=object)
    if form.is_valid():
        update = form.save(commit=False)
        update.save()
        return HttpResponseRedirect(reverse('edit_contact_profile', kwargs={'pk':pk}))
    return render(request, 'profile/forms/edit_user.html', locals())

#########################
#   Edit Hiring data   #
#########################
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def edit_hiring_profile(request, pk):
    btn = 'Ver Perfil'
    btn_url = reverse('profile', kwargs={'pk':pk})
    object = get_object_or_404(User.objects.exclude(is_superuser=1), id=pk)
    u = object.username
    title = 'Editar {0}'.format(u,)
    subtitle = 'Editar información personal'
    hiring, created = models.Hiring.objects.get_or_create(user=object)
    object = get_object_or_404(models.Hiring, user_id=pk)
    form = forms.HiringForm(request.POST or None, instance=object)
    if request.method == 'POST':
        if form.is_valid():
            update = form.save(commit=False)
            update.save()
            messages.add_message(request, messages.INFO, 'This is a success.')
            return HttpResponseRedirect(reverse('edit_hiring_profile', kwargs={'pk':pk}))
        else:
            messages.add_message(request, messages.ERROR, 'This is an error.')
            return HttpResponseRedirect(reverse('edit_hiring_profile', kwargs={'pk':pk}))
    return render(request, 'profile/forms/edit_user.html', locals())

###########################################
#  Show all the contracts in the system   #
###########################################
@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('auth.add_user', login_url='home'), name='dispatch')
class contracts(ListView):
    model = models.Contracts
    paginate_by = 10
    template_name = 'profile/contracts.html'
    def get_queryset(self, *args, **kwargs):
        qs = super(contracts, self).get_queryset(*args, **kwargs).order_by('title')
        return qs
    def get_context_data(self, *args, **kwargs):
        context = super(contracts, self).get_context_data(*args, **kwargs)
        context["title"] = "Contratos"
        context["subtitle"] = "Contratos laborales en el sistema"
        context["btn"] = "Crear contrato"
        context["btn_url"] = reverse("new_contract")
        return context

#############################
#   Create a New Contract   #
#############################
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def new_contract(request):
    btn = 'Cancelar'
    btn_url = reverse('contracts')
    #object = models.Contracts.object
    #hiring, created = models.Contracts.objects.get_or_create(hiring=object)
    #object = get_object_or_404(models.Hiring, user_id=pk)
    form = forms.ContractsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            update = form.save(commit=False)
            update.save()
            messages.add_message(request, messages.INFO, 'This is a success.')
            return HttpResponseRedirect(reverse('contracts'))
        else:
            messages.add_message(request, messages.ERROR, 'This is an error.')
            return HttpResponseRedirect(reverse('contracts'))
    return render(request, 'profile/forms/contracts.html', locals())


#######################
#   Render Contract   #
#######################
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def contract(request, pk):
    subtitle = 'Vista Previa'
    btn = 'Cerrar'
    btn_url = reverse('contracts')
    object = get_object_or_404(models.Contracts, id=pk)
    subtitle = object.title
    return render(request, 'profile/contract.html', locals())

#####################
#   Edit Contract   #
#####################
@permission_required('auth.change_user', login_url='users')
@login_required (login_url='login')
def edit_contract(request, pk):
    btn = 'Cancelar'
    btn_url = reverse('contracts')
    #object = models.Contracts.object
    #hiring, created = models.Contracts.objects.get_or_create(hiring=object)
    object = get_object_or_404(models.Contracts, id=pk)
    form = forms.ContractsForm(request.POST or None, instance=object)
    if request.method == 'POST':
        if form.is_valid():
            update = form.save(commit=False)
            update.save()
            messages.add_message(request, messages.INFO, 'This is a success.')
            return HttpResponseRedirect(reverse('contracts'))
        else:
            messages.add_message(request, messages.ERROR, 'This is an error.')
            return HttpResponseRedirect(reverse('contracts'))
    return render(request, 'profile/forms/contracts.html', locals())

###################################
#  Delete Contract from the database  #
###################################
@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(permission_required('auth.delete_user', login_url='home'), name='dispatch')
class delete_contract(DeleteView):
    template_name = "users/forms/delete.html"
    model = models.Contracts
    def get_success_url(self):
        return reverse("contracts") 
    def get_context_data(self, *args, **kwargs):
        context = super(delete_contract, self).get_context_data(*args, **kwargs)
        context["title"] = "Eliminar empleado del sistema"
        context["subtitle"] = "Estás a punto de eliminar a este usuario"
        context["btn"] = "Cancelar"
        context["btn_url"] = reverse("users")
        context["page"] = "¿Estás seguro?"
        return context
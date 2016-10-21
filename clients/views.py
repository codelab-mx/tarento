# -*- coding: utf-8 e
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from . import models
from . import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.formsets import formset_factory
import datetime
from django.contrib.auth.models import User

# Class based views
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


##########################################
#  Render all the clients in the system  #
##########################################
class list_clients(ListView):
    model = models.Clients
    paginate_by = 6
    template_name = 'clients/index.html'
    def get_queryset(self, *args, **kwargs):
    	qs = super(list_clients, self).get_queryset(*args, **kwargs).order_by('NAME')
    	print qs 
    	return qs
    def get_context_data(self, *args, **kwargs):
    	context = super(list_clients, self).get_context_data(*args, **kwargs)
    	context["title"] = "Clientes"
    	context["subtitle"] = "Clientes registrados en el sistema"
    	context["btn"] = "Agregar Cliente"
    	context["btn_url"] = reverse("add_new_client")
    	return context


#########################################
#  Register a New Client in the system  #
#########################################
def new_clients(request):
	general = 1
	global foreingkey
	model = User()
	username = request.user.id
	title = "Agregar Nuevo Cliente"
	subtitle = 'Registrar cliente en el sistema'
	btn = 'Cancelar'
	btn_url = reverse('clients_dashboard')
	form = forms.new_client(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			f = form.save(commit = False )
			f.save()
			return HttpResponseRedirect(reverse("clients_dashboard"))

	return render(request, 'clients/form.html', locals())

#########################################
#  Edit a Client in the system 		    #
#########################################
def edit_client(request, pk):
   title = 'Editar Información de Cliente'    
   btn = 'Ver Cliente'
   btn_url = reverse('profile_client', kwargs={'pk':pk})
   object = get_object_or_404(models.Clients.objects, id=pk)
   client = object.NAME
   title = 'Editar {0}'.format(client)
   subtitle = 'Editar información personal'
   form = forms.new_client(request.POST or None, instance=object)
   if form.is_valid():
       update = form.save(commit=False)
       update.save()
       return HttpResponseRedirect(reverse("clients_dashboard"))
       #return HttpResponseRedirect(reverse('profile', kwargs={'pk':pk}))
   return render(request, 'clients/form.html', locals())


#####################################
#  Delete Client from the database  #
#####################################

#@method_decorator(login_required(login_url='login'), name='dispatch')
#@method_decorator(permission_required('auth.delete_user', login_url='home'), name='dispatch')
class delete_client(DeleteView):
	template_name = "clients/delete.html"
	model = models.Clients
	def get_success_url(self):
		return reverse("clients_dashboard")	
	def get_context_data(self, *args, **kwargs):
		context = super(delete_client, self).get_context_data(*args, **kwargs)
		context["title"] = "Eliminar cliente del sistema"
		context["subtitle"] = "Estás a punto de eliminar a este cliente"
		context["btn"] = "Cancelar"
		context["btn_url"] = reverse("clients_dashboard")
		context["page"] = "¿Estás seguro?"
		return context

def profile_clients(request, pk):
	object = get_object_or_404(models.Clients.objects, id=pk)
	btn = 'Cancelar'
	btn_url = reverse('clients_dashboard')
	client = object.NAME
	title = 'Editar {0}'.format(client)
	subtitle = 'Editar información del Cliente'
	return render(request, 'clients/client_profile.html', locals())


def calendar(request):
	#object = get_object_or_404(models.Clients.objects, id=pk)
	btn = 'Cancelar'
	btn_url = reverse('clients_dashboard')
	subtitle = 'Calendario de Citas y Actividades'
	return render(request, 'clients/calendar.html', locals())
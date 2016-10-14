from django.shortcuts import render
from django.core.urlresolvers import reverse
from . import models
from . import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.formsets import formset_factory
import datetime

##########################################
#  Render all the clients in the system  #
##########################################
def list_clients(request):
	subtitle = 'Clientes registrados en el sistema'
	title = "Clientes" 
	btn = "Agregar Cliente"
	btn_url = reverse('add_new_client')
	flag = False
	return render(request, 'clients/index.html', locals())

#########################################
#  Register a New Client in the system  #
#########################################
def new_clients(request):
	title = "Agregar Nuevo Cliente"
	subtitle = 'Registrar cliente en el sistema'
	btn = 'Cancelar'
	btn_url = reverse('clients_dashboard') 
	form_1 = forms.new_client_general(request.POST or None)
	form_2 = forms.new_client_contact(request.POST or None)
	form_3 = forms.new_client_address(request.POST or None)
	form_4 = forms.new_client_additional(request.POST, request.FILES)
	if form_2.is_valid():
		f=form_2.save(commit = False)
		f.save()
		return HttpResponseRedirect(reverse("clients_dashboard"))
	return render(request, 'clients/form.html', locals())
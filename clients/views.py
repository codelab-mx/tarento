from django.shortcuts import render
from django.core.urlresolvers import reverse
from . import models
from .forms import new_client
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.formsets import formset_factory
from models import General_Clients
import datetime



def list_clients(request):
	flag = False
	title = "Clientes" 
	btn = "Agregar Cliente"
	btn_url = reverse('add_new_client')
	return render(request, 'clients/index.html', locals())


def new_clients(request):
	title = "Agregar Nuevo Cliente" 
	form_1 = new_client(request.POST or None)
	model = General_Clients()
	if form_1.is_valid():
		f=form_1.save(commit = False)
		f.save()
		return HttpResponseRedirect(reverse("clients_dashboard"))
	return render(request, 'clients/form.html', locals())
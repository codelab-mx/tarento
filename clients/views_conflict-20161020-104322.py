from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from . import models
from . import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.formsets import formset_factory
import datetime
from django.contrib.auth.models import User
from django.views.generic import ListView



##########################################
#  Render all the clients in the system  #
##########################################
class list_clients(ListView):
    model = models.General
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
	form_1 = forms.new_client_general(request.POST or None)
	form_2 = forms.new_client_contact(request.POST or None)
	form_3 = forms.new_client_address(request.POST or None)
	form_4 = forms.new_client_additional(request.POST, request.FILES)
	object = get_object_or_404(form_1.objects, id=pk)
	if form_1.is_valid() and form_2.is_valid() and form_3.is_valid() and form_4.is_valid():
		f_1=form_1.save(commit = False)
		f_1.VENDOR = username
		print pk
		f_2=form_2.save(commit = False)
		f_2.save()
		f_3=form_3.save(commit = False)
		f_3.save()
		f_4=form_4.save(commit = False)
		f_4.save()
		return HttpResponseRedirect(reverse("clients_dashboard"))
	return render(request, 'clients/form.html', locals())


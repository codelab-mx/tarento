from django.shortcuts import render

# Create your views here.

def list_clients(request):
	flag = False
	title = "Clientes" 
	return render(request, 'clients/index.html', locals())


def new_clients(request):
	title = "Agregar Nuevo Cliente" 
	return render(request, 'clients/new_form.html', locals())
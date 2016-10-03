from django.shortcuts import render

# Create your views here.

def list_clients(request):
	return render(request, 'clients/index.html', locals())
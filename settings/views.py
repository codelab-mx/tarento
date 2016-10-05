from django.shortcuts import render, render_to_response 

def home(request):
	return render(request, "dashboard.html", locals())

def login_crm(request):
	return render(request, "dashboard.html", locals())

def logout_crm(request):
	return render(request, "dashboard.html", locals())
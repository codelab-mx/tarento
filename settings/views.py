# -*- coding: utf-8
#get a random value from dictionary
import random
# django decorators for login and permission purpose
from django.contrib.auth.decorators import login_required, permission_required
# django login and logout modules
from django.contrib.auth import logout, authenticate, login, get_user_model
#django required modules for send email
import smtplib
from email.mime.text import MIMEText
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
#django render modules
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
#django forms such as Login and ContactForm
from . import forms
#get the static url on views url = static('x.jpg')
from django.contrib.staticfiles.templatetags.staticfiles import static


#####################
#  DASHBOARD PAGE   #
#####################
@login_required (login_url='/login/')
def home(request):
	return render(request, 'dashboard.html', locals())


################
#  LOGIN PAGE  #
################
def login_crm(request):
	title = 'Accede a nuestro portal de clientes'
	page = 'Login'
	static_url = 'img/login/login.jpg'
	background = static(static_url)
	form = forms.UserLoginForm(request.POST or None)
	if request.user.is_active:
		return HttpResponseRedirect(reverse('home'))
	elif form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect(reverse('home'))
	return render(request, 'login.html', locals())

##############
#   LOGOUT   #
##############
@login_required (login_url='/login/')
def logout_crm(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))
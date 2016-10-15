from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

####################################
# model to expand the user profile #
####################################
class Profile(models.Model):
	user = models.OneToOneField(User)
	curp = models.CharField(max_length=20, blank=True)
	social_number = models.CharField(max_length=15, null=True, blank=True, unique=True)
	rfc = models.CharField(max_length=15, null=True, blank=True, unique=True)
	birthday = models.DateField(null=True, blank=True)
	address = models.CharField(max_length=200, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	cellphone = models.CharField(max_length=20, blank=True)
	education_degree = models.CharField(max_length=150, blank=True)
	gender = models.CharField(max_length=10, blank=True)
	blood_type = models.CharField(max_length=50, blank=True)

class Contact(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=50, blank=True)
	last_name = models.CharField(max_length= 100, blank=True)
	cellphone = models.CharField(max_length=20, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	email = models.CharField(max_length=100, blank=True)
	observations = models.CharField(max_length=250, blank=True)

###############
# Hiring data #
###############
class Hiring(models.Model):
	user = models.OneToOneField(User)
	job_position = models.CharField(max_length=100, blank=True)
	hire_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	bank_name = models.CharField(max_length=50, blank=True)
	clabe = models.CharField(max_length=15, blank=True)

#########################
# Model form to Profile #
#########################
class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ('user',)

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		exclude = ('user',)

class HiringForm(ModelForm):
	class Meta:
		model = Hiring
		exclude = ('user',)

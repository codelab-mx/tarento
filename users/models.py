from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
class Contracts(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()

class Profile(models.Model):
	user = models.OneToOneField(User)
	contract = models.OneToOneField(Contracts)
	curp = models.CharField(max_length=200)
	social_number = models.PositiveIntegerField()
	rfc = models.PositiveIntegerField()
	birthday = models.CharField(max_length=200)
	hire_date = models.CharField(max_length=200)
	
class ContractsForm(ModelForm):
	class Meta:
		model = Contracts
		fields = '__all__'

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'

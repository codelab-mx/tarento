# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from . import models
from settings.my_forms import as_myp

###############
#   choices   #
###############
BloodChoices = (
	('', 'Selecciona un tipo de Sangre'),
	('O-', 'Tipo O-'),
	('O+', 'Tipo O+'),
	('A-', 'Tipo A-'),
	('A+', 'Tipo A+'),
	('B-', 'Tipo B-'),
	('B+', 'Tipo B+'),
	('AB-', 'Tipo AB-'),
	('AB+', 'Tipo AB+'),
	)

GenderChoices = (
	('', 'Selecciona un Genero'),
	('M', 'Masculino'),
	('F', 'Femenino'),
	)

RelationshipChoices = (
	('', 'Selecciona una Opción'),
	('Conyugue', 'Es su Conyugue'),
	('Padre/Madre', 'Es su Padre o Madre'),
	('Hij(a)', 'Es su Hijo(a)'),
	('Herman(a)', 'Es su Hermano(a)'),
	('Ninguno', 'No tiene parentesco'),
	)
################
#   UserForm   #
################
class UserRegisterForm(forms.ModelForm):
	username = forms.CharField(label='@Usuario *', widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario', 'class': 'form-control'}), validators=[RegexValidator(regex='^.{4,15}$', message='Este campo debe tener 4 a 10 carácteres', code='nomatch')])
	email = forms.EmailField(label='Email*', widget=forms.TextInput(attrs={'placeholder': 'Dirección de correo electrónico', 'class': 'form-control'}))
	first_name = forms.CharField(label='Nombre(s) *', widget=forms.TextInput(attrs={'placeholder': 'Nombre(s)', 'class': 'form-control'}))
	last_name = forms.CharField(label='Apellido(s) *', widget=forms.TextInput(attrs={'placeholder': 'Apellido(s)', 'class': 'form-control'}))
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']
	def clean_username(self):
		return self.cleaned_data.get('username').lower()
	def clean_first_name(self):
		return self.cleaned_data.get('first_name').title()
	def clean_last_name(self):
		return self.cleaned_data.get('last_name').title()
	as_myp = as_myp

class UserChangePassword(forms.ModelForm):
	password = forms.CharField(label='Contraseña Nueva', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}))
	password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña', 'class': 'form-control'}))
	class Meta:
		model = User
		fields = ['password', 'password2']
	def clean_password2(self):
		password2 = self.cleaned_data.get('password2')
		password = self.cleaned_data.get('password')
		if password2 != password:
			raise forms.ValidationError('Las contraseñas no coinciden')



####################
#   Profile form   #
####################
class ProfileForm(forms.ModelForm):
	curp = forms.CharField(required=False, label='C.U.R.P.', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	rfc = forms.CharField(required=False, label='R.F.C.', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	social_number = forms.CharField(required=False, label='Número de Seguro Social', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	birthday = forms.DateTimeField(required=False, label='Fecha de Cumpleaños', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	address = forms.CharField(required=False, label='Dirección', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	phone = forms.CharField(required=False, label='Teléfono de Casa', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	cellphone = forms.CharField(required=False, label='Número Celular', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	education_degree = forms.CharField(required=False, label='Escolaridad', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	blood_type = forms.CharField(required=False, label='Grupo Sanguíneo', widget=forms.Select(choices=BloodChoices, attrs={'class': 'form-control'}))	
	gender = forms.CharField(required=False, label='Genero', widget=forms.Select(choices=GenderChoices, attrs={'class': 'form-control'}))
	def clean_rfc(self):
		return self.cleaned_data.get('rfc').upper()
	def clean_curp(self):
		return self.cleaned_data.get('curp').upper()
	class Meta:
		model = models.Profile
		exclude = ('user',)
	as_myp = as_myp

####################
#   Contact Form   #
####################
class ContactForm(forms.ModelForm):
	first_name = forms.CharField(required=False, label='Nombre(s)', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	last_name = forms.CharField(required=False, label='Apellido(s)', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	cellphone = forms.CharField(required=False, label='Teléfono Celular', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	phone = forms.CharField(required=False, label='Teléfono Particular', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	email = forms.EmailField(required=False, label='Email', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	observations = forms.CharField(required=False, label='Parentesco', widget=forms.Select(choices=RelationshipChoices, attrs={'class': 'form-control'}))
	def clean_first_name(self):
		return self.cleaned_data.get('first_name').title()
	def clean_last_name(self):
		return self.cleaned_data.get('last_name').title()
	class Meta:
		model = models.Contact
		#cc
		exclude = ('user',)
	as_myp = as_myp

####################
#   Hiring Form   #
####################
class HiringForm(forms.ModelForm):
	#contract = forms.ModelChoiceField(required=False, label='Tipo de Contrato', queryset=models.Contracts.objects.all(), widget=forms.Select(attrs={ 'class':  'form-control'}))
	job_position = forms.CharField(required=False, label='Puesto', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	hire_date = forms.DateTimeField(required=False, label='Fecha de Contratación', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	end_date = forms.DateTimeField(required=False, label='Fecha de termino', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	bank_name = forms.CharField(required=False, label='Nombre de Banco', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))
	clabe = forms.CharField(required=False, label='Número CLABE', widget=forms.TextInput(attrs={'placeholder':'', 'class':'form-control'}))

	class Meta:
		model = models.Hiring
		exclude = ('user',)
	as_myp = as_myp

######################
#   Contracts Form   #
######################
class ContractsForm(forms.ModelForm):
	title = forms.CharField(required=True, label='Título', widget=forms.TextInput(attrs={'placeholder':'Ejemplo: Prestación de Servicios', 'class':'form-control'}))
	content = forms.CharField(required=True, label='Contenido', widget=forms.Textarea(attrs={'placeholder':'Descripción del contrato', 'class':'form-control wysiwyg mt-lg'}))
	class Meta:
		model = models.Contracts
		fields = '__all__'
	as_myp = as_myp
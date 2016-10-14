# -*- coding: utf-8 e
from django import forms
#from models import General_Clients, Clients_Contact, Clients_Address, Clients_Additional
from . import models
from . import validators
import datetime

now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d %H:%M")

SOURCE_CHOICES = (

	('', 'Selecciona la Fuente de Contacto'),
	('recomndacion empleado', 'Recomendación Empleado'),
	('recomendacion externa', 'Recomendaciónn Externa'),
	('llamada', 'llamada'),
	('chat', 'chat'),
	('cliente existente', 'Cliente Existente'),
	('web', 'Web'),

	)

TYPE_CHOICES = (
	('', 'Selecciona el Tipo de Cliente'),
	('A', 'Tipo A'),
	('B', 'Tipo B'),
	('C', 'Tipo C'),
	('D', 'Tipo D'),
	('T', 'Tipo T'),

	)

STATE_CHOICES = (
	('', 'Selecciona el Estado'),
	('Queretaro', 'Querétaro'),
	)

COUNTRY_CHOICES = (
	('Mexico', 'México'),

	)




class new_client_general(forms.ModelForm):
	
	COMPANY = forms.CharField(required=False, label='Empresa', widget=forms.TextInput(attrs={'placeholder': 'ACME SA de CV', 'class':  'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	NAME = forms.CharField(required=False, label='Nombre Comercial', widget=forms.TextInput(attrs={'placeholder': 'ACME', 'class': 'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	RFC = forms.CharField(required=False, label='RFC', widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: ABC680524P76', 'class': 'form-control'}), validators=[validators.rfc])
	TYPE = forms.CharField(required=False, label='Tipo', widget=forms.Select(choices=TYPE_CHOICES, attrs={'placeholder': 'ACME', 'class': 'form-control'}))	
	SOURCE = forms.CharField(required=False, label='Fuente', widget=forms.Select( choices=SOURCE_CHOICES, attrs={'placeholder': 'ACME', 'class': 'form-control'}))
	PHONE = forms.CharField(required=False, label='Teléfono Empresarial', widget=forms.TextInput(attrs={'placeholder': '+524425555555', 'class': 'form-control'}), validators=[validators.phone])
	DATE_1 = forms.CharField(required=False, widget=forms.HiddenInput(), initial=today)

	class Meta:
		model = models.General
		fields = '__all__'

	def as_myp(self):		
		return self._html_output(
		normal_row = '<div class="col-md-6"><p%(html_class_attr)s>%(label)s</p> <p>%(field)s%(help_text)s</p> %(errors)s</p></div>',
		row_ender = '</p>',
		error_row = '%s',
		help_text_html = ' <span class="helptext">%s</span>',
		errors_on_separate_row = False)

class new_client_contact(forms.ModelForm):
	
	CONTACT_NAME_1 = forms.CharField(required=False, label='Persona de Contacto', widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class':  'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	PHONE_1 = forms.CharField(required=False, label='Telefono', widget=forms.TextInput(attrs={'placeholder': '+524425555555', 'class': 'form-control'}), validators=[validators.phone])
	MAIL_1 = forms.EmailField(required=False, label='Correo Electronico', widget=forms.EmailInput(attrs={'placeholder': 'contacto@mail.com', 'class': 'form-control'}))	
	CONTACT_NAME_2= forms.CharField(required=False, label='Contacto Adicional', widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	PHONE_2 = forms.CharField(required=False, label='Telefono Adicional', widget=forms.TextInput(attrs={'placeholder': '+524425555555', 'class': 'form-control'}), validators=[validators.phone])
	MAIL_2 = forms.EmailField(required=False, label='Correo Adicional', widget=forms.EmailInput(attrs={'placeholder': 'contacto2@mail.com', 'class': 'form-control'}))

	class Meta:
		model = models.Contact
		fields = '__all__'

	def as_myp(self):		
		return self._html_output(
		normal_row = '<div class="col-md-6"><p%(html_class_attr)s>%(label)s</p> <p>%(field)s%(help_text)s</p> %(errors)s</p></div>',
		row_ender = '</p>',
		error_row = '%s',
		help_text_html = ' <span class="helptext">%s</span>',
		errors_on_separate_row = False)

class new_client_address(forms.ModelForm):
	
	STREET_NAME = forms.CharField(required=False, label='Calle y Número', widget=forms.TextInput(attrs={'placeholder': 'Paseo Río Grande 202', 'class':  'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	NEIGHBORHOOD = forms.CharField(required=False, label='Colonia', widget=forms.TextInput(attrs={'placeholder': 'Arquitos', 'class': 'form-control'}), validators=[validators.phone])
	ZIP = forms.CharField(required=False, label='Codigo Postal', widget=forms.TextInput(attrs={'placeholder': '76050', 'class': 'form-control'}))	
	STATE = forms.CharField(required=False, label='Estado', widget=forms.Select(choices=STATE_CHOICES, attrs={'placeholder': 'ACME', 'class': 'form-control'}))	
	CITY= forms.CharField(required=False, label='Municipio', widget=forms.TextInput(attrs={'placeholder': 'Querétaro', 'class': 'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	COUNTRY = forms.CharField(required=False, label='País', widget=forms.Select(choices=COUNTRY_CHOICES, attrs={'placeholder': 'ACME', 'class': 'form-control'}))	

	class Meta:
		model = models.Address
		fields = '__all__'


	def as_myp(self):		
		return self._html_output(
		normal_row = '<div class="col-md-6"><p%(html_class_attr)s>%(label)s</p> <p>%(field)s%(help_text)s</p> %(errors)s</p></div>',
		row_ender = '</p>',
		error_row = '%s',
		help_text_html = ' <span class="helptext">%s</span>',
		errors_on_separate_row = False)

class new_client_additional(forms.ModelForm):
	DESCRIPTION = forms.CharField(required=False, label='Descripcion Adicional', widget=forms.Textarea(attrs={'placeholder': 'Escribe Parámetros Adicionales',  'class':  'form-control note-editor note-editor-margin'}))
	IMAGE = forms.ImageField(required=False, label='Sube el logotipo de la empresa')

	class Meta:
		model = models.Additional
		fields = '__all__'
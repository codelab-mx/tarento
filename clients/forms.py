# -*- coding: utf-8 e
from django import forms
#from models import Clients_Clients, Clients_Contact, Clients_Address, Clients_Additional
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
	('G', 'Tipo G'),
	('T', 'Tipo T'),

	)

STATE_CHOICES = (
	('', 'Selecciona el Estado'),
	('Queretaro', 'Querétaro'),
	)

COUNTRY_CHOICES = (
	('Mexico', 'México'),

	)




class new_client(forms.ModelForm):


	COMPANY = forms.CharField(required=False, label='Razón Social', widget=forms.TextInput(attrs={'placeholder': 'ACME SA de CV', 'class':  'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	NAME = forms.CharField(required=False, label='Cliente', widget=forms.TextInput(attrs={'placeholder': 'ACME', 'class': 'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	RFC = forms.CharField(required=False, label='RFC', widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: ABC680524P76', 'class': 'form-control'}), validators=[validators.rfc])
	TYPE = forms.CharField(required=False, label='Tipo', widget=forms.Select(choices=TYPE_CHOICES, attrs={'placeholder': 'ACME', 'class': 'form-control'}))	
	SOURCE = forms.CharField(required=False, label='Fuente', widget=forms.Select( choices=SOURCE_CHOICES, attrs={'placeholder': 'ACME', 'class': 'form-control'}))
	PHONE = forms.CharField(required=False, label='Teléfono Empresarial', widget=forms.TextInput(attrs={'placeholder': '4425555555', 'class': 'form-control'}), validators=[validators.phone])
	DATE_1 = forms.CharField(required=False, widget=forms.HiddenInput(), initial=today)
	VENDOR = forms.CharField(required=False, widget=forms.HiddenInput())
	CONTACT_NAME_1 = forms.CharField(required=False, label='Persona de Contacto', widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class':  'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	PHONE_1 = forms.CharField(required=False, label='Telefono', widget=forms.TextInput(attrs={'placeholder': '+4425555555', 'class': 'form-control'}), validators=[validators.phone])
	EXT_1 = forms.CharField(required=False, label='Ext', widget=forms.TextInput(attrs={'placeholder': 'EXT', 'class': 'form-control'}), validators=[validators.ext])
	MAIL_1 = forms.EmailField(required=False, label='Correo Electronico', widget=forms.EmailInput(attrs={'placeholder': 'contacto@mail.com', 'class': 'form-control'}))	
	CONTACT_NAME_2= forms.CharField(required=False, label='Contacto Adicional', widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	PHONE_2 = forms.CharField(required=False, label='Telefono Adicional', widget=forms.TextInput(attrs={'placeholder': '+4425555555', 'class': 'form-control'}), validators=[validators.phone])
	EXT_2 = forms.CharField(required=False,  widget=forms.TextInput(attrs={'placeholder': 'EXT', 'class': 'form-control'}), validators=[validators.ext])
	MAIL_2 = forms.EmailField(required=False, label='Correo Adicional', widget=forms.EmailInput(attrs={'placeholder': 'contacto2@mail.com', 'class': 'form-control'}))
	STREET_NAME = forms.CharField(required=False, label='Calle y Número', widget=forms.TextInput(attrs={'placeholder': 'Paseo Río Grande 202', 'class':  'form-control'}))
	NEIGHBORHOOD = forms.CharField(required=False, label='Colonia', widget=forms.TextInput(attrs={'placeholder': 'Arquitos', 'class': 'form-control'}))
	ZIP = forms.CharField(required=False, label='Codigo Postal', widget=forms.TextInput(attrs={'placeholder': '76050', 'class': 'form-control'}), validators=[validators.zip_code])	
	STATE = forms.CharField(required=False, label='Estado', widget=forms.Select(choices=STATE_CHOICES, attrs={'placeholder': 'ACME', 'class': 'form-control'}))	
	CITY= forms.CharField(required=False, label='Municipio', widget=forms.TextInput(attrs={'placeholder': 'Querétaro', 'class': 'form-control'}))
	COUNTRY = forms.CharField(required=False, label='País', widget=forms.Select(choices=COUNTRY_CHOICES, attrs={'placeholder': 'ACME', 'class': 'form-control'}))
	IND_PARK = forms.ModelChoiceField(required=False, queryset=models.Parks.objects.all(), widget=forms.Select(attrs={ 'class':  'form-control'}))
	DESCRIPTION = forms.CharField(required=False, label='Descripcion Adicional', widget=forms.Textarea(attrs={'placeholder': 'Escribe Parámetros Adicionales',  'class':  'form-control note-editor note-editor-margin'}))
	IMAGE = forms.ImageField(required=False, label='Sube el logotipo de la empresa')

	class Meta:
		model = models.Clients
		fields = '__all__'


	def clean_RFC(self):
		return self.cleaned_data.get('RFC').upper()
	def clean_COMPANY(self):
		return self.cleaned_data.get('COMPANY').upper()
	def clean_NAME(self):
		return self.cleaned_data.get('NAME').title()
	def clean_CONTACT_NAME_1(self):
		return self.cleaned_data.get('CONTACT_NAME_1').title()
	def clean_CONTACT_NAME_2(self):
		return self.cleaned_data.get('CONTACT_NAME_2').title()
	def clean_STREET_NAME(self):
		return self.cleaned_data.get('STREET_NAME').title()
	def clean_NEIGHBORHOOD(self):
		return self.cleaned_data.get('NEIGHBORHOOD').title()
	def clean_CITY(self):
		return self.cleaned_data.get('CITY').title()

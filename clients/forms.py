# -*- coding: utf-8 e
from django import forms
from models import General_Clients
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



class new_client(forms.ModelForm):
	
	COMPANY = forms.CharField(required=True, label='Empresa', widget=forms.TextInput(attrs={'placeholder': 'ACME SA de CV', 'class':  'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	NAME = forms.CharField(required=True, label='Nombre Comercial', widget=forms.TextInput(attrs={'placeholder': 'ACME', 'class': 'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	RFC = forms.CharField(required=True, label='RFC', widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: ABC680524P76', 'class': 'form-control'}), validators=[validators.rfc])
	TYPE = forms.CharField(required=True, label='Tipo', widget=forms.Select(choices=TYPE_CHOICES, attrs={'placeholder': 'ACME', 'class': 'form-control'}))	
	SOURCE = forms.CharField(required=True, label='Fuente', widget=forms.Select( choices=SOURCE_CHOICES, attrs={'placeholder': 'ACME', 'class': 'form-control'}))
	PHONE = forms.CharField(required=True, label='Teléfono Empresarial', widget=forms.TextInput(attrs={'placeholder': 'ACME', 'class': 'form-control'}))
	DATE = forms.CharField(required=False, widget=forms.HiddenInput(), initial=today)




	class Meta:
		model = General_Clients
		fields = '__all__'

	def as_myp(self):
		"Returns this form rendered as HTML <p>s."
		return self._html_output(
		normal_row = '<p%(html_class_attr)s>%(label)s</p> <p>%(field)s%(help_text)s</p> %(errors)s</p>',
		row_ender = '</p>',
		error_row = '%s',
		help_text_html = ' <span class="helptext">%s</span>',
		errors_on_separate_row = False)



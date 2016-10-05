# -*- coding: utf-8 
from django import forms
from models import General_Clients
from . import validators

class new_client(forms.ModelForm):
	
	COMPANY = forms.CharField(required=True, label='Empresa', widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validators.lenght_min, validators.lenght_max])
	NAME = forms.CharField(required=True, label='Nombre Comercial', widget=forms.TextInput(attrs={'class': 'form-control'}))
	RFC = forms.CharField(required=True, label='RFC', widget=forms.TextInput(attrs={'class': 'form-control'}))
	TYPE = forms.CharField(required=True, label='Tipo', widget=forms.TextInput(attrs={'class': 'form-control'}))
	SOURCE = forms.CharField(required=True, label='Fuente', widget=forms.TextInput(attrs={'class': 'form-control'}))
	PHONE = forms.CharField(required=True, label='Teléfono Empresarial', widget=forms.TextInput(attrs={'class': 'form-control'}))
	DATE = forms.CharField(required=False, widget=forms.HiddenInput(), initial="")

	class Meta:
		model = General_Clients
		fields = '__all__'


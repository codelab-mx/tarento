# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from settings.my_forms import as_myp
#User = get_user_model()

class UserRegisterForm(forms.ModelForm):
	username = forms.CharField(label='@Usuario *', widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario', 'class': 'form-control'}), validators=[RegexValidator(regex='^.{4,20}$', message='Este campo debe tener 4 a 20 carácteres', code='nomatch')])
	email = forms.EmailField(label='Email *', widget=forms.TextInput(attrs={'placeholder': 'Dirección de correo electrónico', 'class': 'form-control'}))
	first_name = forms.CharField(label='Nombre(s) *', widget=forms.TextInput(attrs={'placeholder': 'Nombre(s)', 'class': 'form-control'}))
	last_name = forms.CharField(label='Apellido(s) *', widget=forms.TextInput(attrs={'placeholder': 'Apellido(s)', 'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}), label='Contraseña *')
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña', 'class': 'form-control'}), label='Confirmar Contraseña *')
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
	def clean_username(self):
		return self.cleaned_data.get('username').lower()
	def clean_first_name(self):
		return self.cleaned_data.get('first_name').title()
	def clean_last_name(self):
		return self.cleaned_data.get('last_name').title()
	def clean_password2(self):
		password2 =self.cleaned_data.get('password2')
		password = self.cleaned_data.get('password')
		if password2 != password:
			raise forms.ValidationError('Las contraseñas no coinciden')
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

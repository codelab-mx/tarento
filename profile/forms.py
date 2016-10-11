# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

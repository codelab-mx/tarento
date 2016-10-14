from __future__ import unicode_literals

from django.db import models

# Create your models here.

class General(models.Model):
	COMPANY = models.CharField( max_length = 50)
	NAME = models.CharField( max_length = 50)
	RFC = models.CharField( max_length = 50, unique=False)
	TYPE = models.CharField( max_length = 50)
	SOURCE = models.CharField( max_length = 50)
	PHONE = models.CharField( max_length = 50)
	DATE_1 = models.CharField(blank = True, max_length = 50)


class Contact(models.Model):
	CONTACT_NAME_1 = models.CharField( max_length = 50)
	PHONE_1 = models.CharField( max_length = 50)
	MAIL_1 = models.EmailField( max_length = 50)
	CONTACT_NAME_2 = models.CharField( max_length = 50)
	PHONE_2 = models.CharField( max_length = 50)
	MAIL_2 = models.EmailField( max_length = 50)

class Address(models.Model):
	STREET_NAME = models.CharField( max_length = 50)
	NEIGHBORHOOD = models.CharField(max_length =50)
	ZIP = models.CharField( max_length = 50)
	CITY = models.CharField( max_length = 50)
	STATE = models.CharField( max_length = 50)
	COUNTRY = models.CharField( max_length = 50)


class Additional(models.Model):
	DESCRIPTION = models.CharField( max_length = 50)
	IMAGE = models.ImageField(upload_to='clients/')
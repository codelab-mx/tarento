from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Clients(models.Model):
	COMPANY = models.CharField(blank = True, max_length = 50,  unique=False)
	NAME = models.CharField(blank = True, max_length = 50)
	RFC = models.CharField(blank = True, max_length = 50, unique=False)
	TYPE = models.CharField(blank = True, max_length = 50)
	SOURCE = models.CharField(blank = True, max_length = 50)
	PHONE = models.CharField(blank = True, max_length = 50)
	DATE_1 = models.CharField(blank = True, max_length = 50)
	VENDOR = models.CharField(blank = True, max_length = 50)
	CONTACT_NAME_1 = models.CharField(blank = True, max_length = 50)
	PHONE_1 = models.CharField(blank = True, max_length = 50)
	EXT_1 = models.CharField(blank = True, max_length = 10)
	MAIL_1 = models.EmailField(blank = True, max_length = 50)
	CONTACT_NAME_2 = models.CharField(blank = True, max_length = 50)
	PHONE_2 = models.CharField(blank = True, max_length = 50)
	EXT_2 = models.CharField(blank = True, max_length = 10)
	MAIL_2 = models.EmailField(blank = True, max_length = 50)
	STREET_NAME = models.CharField(blank = True, max_length = 50)
	NEIGHBORHOOD = models.CharField(blank = True,max_length =50)
	ZIP = models.CharField(blank = True, max_length = 50)
	CITY = models.CharField(blank = True, max_length = 50)
	STATE = models.CharField(blank = True, max_length = 50)
	COUNTRY = models.CharField(blank = True, max_length = 50)
	IND_PARK = models.ForeignKey('Parks', blank = True, null = True)
	DESCRIPTION = models.CharField(blank = True, max_length = 500)
	IMAGE = models.ImageField(blank = True, upload_to='clients/')

class Parks(models.Model):
	IND_PARK = models.CharField(max_length = 50)

	class Meta:
		ordering = ('IND_PARK',)
	def __unicode__(self):
		return self.IND_PARK

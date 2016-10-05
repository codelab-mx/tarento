from __future__ import unicode_literals

from django.db import models

# Create your models here.

class General_Clients(models.Model):
	COMPANY = models.CharField(blank = True, max_length = 50)
	NAME = models.CharField(blank = True, max_length = 50)
	RFC = models.CharField(blank = True, max_length = 50)
	TYPE = models.CharField(blank = True, max_length = 50)
	SOURCE = models.CharField(blank = True, max_length = 50)
	PHONE = models.CharField(blank = True, max_length = 50)
	DATE = models.CharField(blank = True, max_length = 50)
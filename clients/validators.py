# -*- coding: utf-8 
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


def lenght_min(value):
	minimum = 4
	if len(value) < minimum:
		raise ValidationError(_('%(value)s debe ser mas largo'), params={'value': value}, )
	return

def lenght_max(value):
	required_css_class = "required"
	error_css_class = "edwin"
	maximum = 10
	if len(value) > maximum:

		raise ValidationError(_('<span class="red">%(value)s debe ser mas corto</span>'), params={'value': value},)
	return

#join([u'<span class="red">%s</span>'
	#class='parsley-required'





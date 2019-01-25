from .models import *
from django.forms import ModelForm


class Email_form(ModelForm):
	class Meta:
		model = Email_model
		fields = '__all__'

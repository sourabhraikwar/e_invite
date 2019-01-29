from .models import *
from django.forms import *
from django import *


class Email_form(ModelForm):
	password = CharField(widget=forms.PasswordInput)
	class Meta:
		model = Email_model
		fields = '__all__'

class SendMailForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = sendEmails
		fields = '__all__'

class CardForm(forms.ModelForm):
	file = forms.FileField(label='Add file')
	class Meta:
		model = addCards
		fields = '__all__'

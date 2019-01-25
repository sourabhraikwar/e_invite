from django.db import models

# Create your models here.
class Email_model(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=30)	
	status = models.CharField(max_length=2, default="0")

class sendEmails(models.Model):
	to = models.EmailField()
	subject = models.CharField(max_length=255)
	message = models.CharField(max_length=255)
		
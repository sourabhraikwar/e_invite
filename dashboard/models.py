from django.db import models

# Create your models here.
class Email_model(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length = 30)
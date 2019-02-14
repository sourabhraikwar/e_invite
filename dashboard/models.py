from django.db import models

# Create your models here.
class Email_model(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=30)	
	status = models.CharField(max_length=2, default=1)

class sendEmails(models.Model):
	to = models.EmailField()
	subject = models.CharField(max_length=255)
	message = models.CharField(max_length=255)


class addCards(models.Model):
	image = models.ImageField(upload_to='uploads/%Y/%m/%d/image', blank=True)
	file = models.FileField(upload_to='uploads/%Y/%m/%d/jsfiles', blank=True)
	audio = models.FileField(upload_to='uploads/%Y/%m/%d/audiofiles', blank=True)
	category = models.CharField(max_length=20, blank=True)


class createdVideos(models.Model):
	output = models.FileField(upload_to='uploads/%Y/%m/%d/output_file', blank=True)
	user_rel = models.CharField(max_length=20)
		
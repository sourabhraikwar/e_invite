from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def dashboard(request):

	context = {
		'title': 'Dashboard'
	}
	return render(request, 'dashboard/dashboard.html', context)

def usersList(request):

	context = {
		'title': 'Users List'
	}
	return render(request, 'dashboard/users-list.html', context)

def cardsList(request):

	context = {
		'title': 'Cards List'
	}
	return render(request, 'dashboard/cards-list.html', context)

def emails(request):
	send_data = SendMailForm()

	if request.method == 'POST':
		send_data = SendMailForm(request.POST)
		if send_data.is_valid():
			cred = Email_model.objects.all()

			for x in cred:
				if x.status == '1':
					usermail=x.email
					userpass=x.password
			print(send_data)
			sub = send_data.cleaned_data['subject']
			msg = send_data.cleaned_data['message']
			to = send_data.cleaned_data['to']
			from_email = usermail
			res = send_mail(sub,msg,from_email, [to], fail_silently=False,auth_user=usermail, auth_password=userpass)
			print(res)
			if res == True:
				send_data.save()
				return HttpResponse('mail send successfully')

	context = {
		'title': 'Email',
		'send_data': send_data,
	}
	return render(request, 'dashboard/emails.html', context)

def settings(request):

	email_form = Email_form()

	if request.method == 'POST':
		
		email_form = Email_form(request.POST)
		print(email_form)
		if email_form.is_valid():
			email_form.save()
			return HttpResponse('Form saved successfully')

	context = {
		'title': 'Settings',
		'smtp_form': email_form,
	}

	return render(request, 'dashboard/settings.html', context)

def profile(request):

	context = {
		'title': 'Profile'
	}
	return render(request, 'dashboard/profile.html', context)

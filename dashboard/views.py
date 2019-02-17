from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from datetime import datetime
from .forms import *
from .models import *
import os, socket
# Create your views here.

def dashboard(request):
	"""this method containing dashboard functionality"""
	video_list = createdVideos.objects.filter(user_rel=request.user.id)
	context = {
		'title': 'Dashboard',
		'videos': video_list
	}
	return render(request, 'dashboard/dashboard.html', context)

def usersList(request):
	data = User.objects.values()
	context = {
		'title': 'Users List',
		'data':data
	}
	return render(request, 'dashboard/users-list.html', context)

def cardsList(request):
	cards_data = addCards.objects.all()
	cardform = CardForm()
	if request.method == 'POST':
		cardform = CardForm(request.POST, request.FILES)
		if cardform.is_valid():
			cardform.save()
			# return HttpResponse('Card Saved Successfully')

		
	context = {
		'title': 'Cards List',
		'cardform': cardform,
		'cards_data': cards_data
		# 'cards':cards,
	}
	return render(request, 'dashboard/cards-list.html', context)

def weddingCardsList(request):
	cat_wedding ='wedding'
	id = "1"
	cards_data = addCards.objects.filter(category=cat_wedding)
	cardform = CardForm()
	if request.method == 'POST':
		cardform = CardForm(request.POST, request.FILES)
		if cardform.is_valid():
			cardform.save()
			# return HttpResponse('Card Saved Successfully')

		
	context = {
		'title': 'Wedding Cards',
		'cardform': cardform,
		'cards_data': cards_data
		# 'cards':cards,
	}
	return render(request, 'dashboard/cards/wedding_cards.html', context)

def birthdayCardsList(request):
	cat_birth = "birthday"
	cards_data = addCards.objects.filter(category=cat_birth)
	cardform = CardForm()
	if request.method == 'POST':
		cardform = CardForm(request.POST, request.FILES)
		if cardform.is_valid():
			cardform.save()
			# return HttpResponse('Card Saved Successfully')

		
	context = {
		'title': 'Birthday Cards',
		'cardform': cardform,
		'cards_data': cards_data
		# 'cards':cards,
	}
	return render(request, 'dashboard/cards/birthday_cards.html', context)

def inaugurationcardsList(request):
	cat_inaug = "inauguration"
	cards_data = addCards.objects.filter(category=cat_inaug)
	cardform = CardForm()
	if request.method == 'POST':
		cardform = CardForm(request.POST, request.FILES)
		if cardform.is_valid():
			cardform.save()
			# return HttpResponse('Card Saved Successfully')

		
	context = {
		'title': 'Inauguration Cards',
		'cardform': cardform,
		'cards_data': cards_data
		# 'cards':cards,
	}
	return render(request, 'dashboard/cards/inauguration_cards.html', context)

def editCard(request, id):
	card_data = addCards.objects.filter(id=id)
	context = {
		'title': 'Edit Card',
		'card_data': card_data
	}
	return render(request, 'dashboard/edit-card.html', context)	

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
			sub = send_data.cleaned_data['subject']
			msg = send_data.cleaned_data['message']
			to = send_data.cleaned_data['to']
			from_email = usermail
			res = send_mail(sub,msg,from_email, [to], fail_silently=False,auth_user=usermail, auth_password=userpass)
			if res == True:
				send_data.save()
				messages.success(request, 'Mail sent successfully!')
				return HttpResponseRedirect('/dashboard/emails')


	data = sendEmails.objects.all()
	context = {
		'title': 'Email',
		'send_data': send_data,
		'data': data,

	}
	return render(request, 'dashboard/emails.html', context)

def settings(request):

	smtp_active_mail = Email_model.objects.filter(status=1)
	email_form = Email_form()

	if request.method == 'POST':
		
		email_form = Email_form(request.POST)
		if email_form.is_valid():
			email = email_form.cleaned_data['email']
			password = email_form.cleaned_data['password']
			smtp_active_mail.update(email=email, password=password, status=1)

	context = {
		'title': 'Settings',
		'smtp_form': email_form,
		'smtp_active_mail': smtp_active_mail
	}

	return render(request, 'dashboard/settings.html', context)
	
def profile(request):

	context = {
		'title': 'Profile'
	}
	return render(request, 'dashboard/profile.html', context)

def videoCreation(request):

	if request.method == 'POST':
		base_dir = "media/"
		path =  "card_video_file/" + request.user.username + "/"
		card_id = request.POST['card_id']
		host = "http://"+request.META['HTTP_HOST']
		extension = ".webm"
		raw_file = base_dir + path + "video_file_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + extension
		output_file =  path + "output"+ datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + extension
		
		if not os.path.exists(base_dir + path):
			os.makedirs(base_dir + path)

		
		with open(raw_file, 'wb+') as destination:
			for chunk in request.FILES['blob'].chunks():
				destination.write(chunk)

		card_data = addCards.objects.filter(id=card_id)

		for x in card_data:
			audio_url = x.audio.url

		os.system("ffmpeg -i "+raw_file+" -i "+host+audio_url+" -c copy -map 0:0 -map 1:0 " + base_dir + output_file)
		vid = createdVideos(output=output_file, user_rel=request.user.id)
		vid.save()

		if os.path.isfile(raw_file):
		    os.remove(raw_file)

	data = {
		"success_data": "successfully saved"
	}

	return JsonResponse(data)



# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from .forms import *
from django.http import HttpResponse

from selenium import webdriver
from PIL import Image
from io import BytesIO

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
# Create your views here.
def home(request):

	context = {
		'title': 'Home'
	}

	return render(request, 'home.html', context)

def Forms(request):
	form = E_Form()
	return render (request, 'home.html', {'form': form})

frame = 0
def on_draw(request):

    pyglet.image.get_buffer_manager().get_color_buffer().save(str(frame)+'.png')
    return render(request, 'home.html')

def fire(request):

	opts = Options()
	opts.set_headless()
	assert opts.headless  # Operating in headless mode
	fox = Firefox(options=opts)
	# fox = webdriver.Firefox(executable_path="/home/webllisto/bin/geckodriver")
	fox.get('http://localhost:8000')
	# now that we have the preliminary stuff out of the way time to get that image :D
	element = fox.find_element_by_id('html') # find part of the page you want image of
	location = element.location
	size = element.size
	png = fox.get_screenshot_as_png() # saves screenshot of entire page
	fox.quit()

	im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

	left = location['x']
	top = location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']


	im = im.crop((left, top, right, bottom)) # defines crop points
	print(im)
	im.save('screenshot.png') # saves new cropped image
	return HttpResponse('task complited')

def browser_scrap(request):
	opts = Options()
	opts.set_headless()
	assert opts.headless  # Operating in headless mode
	browser = Firefox(options=opts)
	browser.get('https://duckduckgo.com')
	search_form = browser.find_element_by_id('search_form_input_homepage')
	search_form.send_keys('real python')
	search_form.submit()
	results = browser.find_elements_by_class_name('result')
	browser.close()
	quit()
	return render(request, 'duck_scrap.html')
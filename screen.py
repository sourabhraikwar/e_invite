from selenium import webdriver
from PIL import Image
from io import BytesIO

fox = webdriver.Firefox(executable_path="/home/webllisto/bin/geckodriver")
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
im.save('screenshot.png') # saves new cropped image

from selenium import webdriver
import time
import os
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
prefs = {"download.default_directory" : "/home/lap01/Py_Virtual/e_invite/media/cards_videos"}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=options, executable_path="chromedriver")
driver.get('http://192.168.1.34:8000/accounts/login/')

# import pdb;pdb.set_trace()

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys("webllisto")
password.send_keys("1234")

driver.find_element_by_id("submit").click()

driver.get('http://192.168.1.34:8000/dashboard/edit_card/5')
driver.find_element_by_id('start').click()
time.sleep(5)
driver.find_element_by_id('download').click()

os.system("ffmpeg -i /home/lap01/Py_Virtual/e_invite/media/cards_videos/test.webm -i /home/lap01/Py_Virtual/e_invite/media/audio/audio.ogg -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac -b:a 192k output.webm")

driver.close()

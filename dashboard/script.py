from selenium import webdriver
import time
import os
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--headless")
prefs = {"download.default_directory" : "/home/webllisto/workspace/e_invite/static/media"}
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

os.system("ffmpeg -i ../static/media/test.webm -i ../static/media/test_aud.ogg -c copy -map 0:0 -map 1:0 Output.webm")

# driver.close()

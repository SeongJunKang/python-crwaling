from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import re
import os

# dir
dirPath = "../한식문화사전"
try:
	if not (os.path.isdir(dirPath)):
		os.makedirs(os.path.join(dirPath))
except OSError as e:
	print("{0} Failed to create directory!!!!!".format(dirPath))

chromedriver = '../../chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

f = open('list.txt')
lines = f.readlines()
for line in lines:
	line = line.rstrip("\n")
	try:
		driver.get(line)
		title = driver.find_elements_by_css_selector('.initial_title')[0].text
		title = re.sub(r"[\\|\/|\:|\*|\?|\"|\<|\>|\|]", '', title)
		containers = driver.find_elements_by_css_selector('.right_container')
		download = open("download/{0}.xml".format(title), mode="wt", encoding="utf-8");
		for contents in containers:
			download.write(contents.get_attribute("innerHTML"))
	except:
		print('{0}에서 에러가 발생했습니다.'.format(line));
driver.quit()

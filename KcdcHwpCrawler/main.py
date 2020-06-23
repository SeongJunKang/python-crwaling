from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

def selector_find(driver):
	element = driver.find_elements_by_css_selector('.add_file_item a')
	if element:
		return element
	else:
		return False

dirPath = "download"
try:
	if not (os.path.isdir(dirPath)):
		os.makedirs(os.path.join(dirPath))
except OSError as e:
	print("{0} Failed to create directory!!!!!".format(dirPath))

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
	"download.default_directory": "{0}\\download".format(os.getcwd()),
	"download.prompt_for_download": False,
	"download.directory_upgrade": True,
	"safebrowsing_for_trusted_sources_enabled": False,
	"safebrowsing.enabled": False
})

chromedriver = 'chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver,chrome_options=options)

list = open('list.txt')
url_list = list.readlines()
for url in url_list:
	driver.get(url)
	try:
		a_tag_list = WebDriverWait(driver, 2).until(selector_find)
		for a in a_tag_list:
			if ".hwp" in a.text:
				a.click()
				time.sleep(1.5)
	except:
		print('ERROR {0}'.format(url))

driver.quit()

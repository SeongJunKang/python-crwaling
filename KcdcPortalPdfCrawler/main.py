from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

def selector_find(driver):
	element = driver.find_elements_by_css_selector('.boardForm td.L a')
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
numbers = list.readlines()
for number in numbers:
	url = "http://www.cdc.go.kr/npt/biz/npp/portal/nppIssueIcdView.do?issueIcdSn={0}".format(number.rstrip("\n"))
	driver.get(url)
	try:
		pdfList = WebDriverWait(driver, 2).until(selector_find)
		for pdf in pdfList:
			pdf.click()
			time.sleep(1.5)
	except:
		print('ERROR {0}'.format(number))

driver.quit()

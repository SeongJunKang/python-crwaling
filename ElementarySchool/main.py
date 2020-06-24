from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import threading
import time
import os

def selector_find(driver):
	element = driver.find_elements_by_css_selector('.fileimg>li>a')
	if element:
		return element
	else:
		return False

def selenium_crawler(school : list):
	chromedriver = '../chromedriver/chromedriver.exe'
	for url in school:
		driver = webdriver.Chrome(chromedriver)
		url = "{0}&listCo=1500".format(url.rstrip("\n"))
		driver.get(url)
		linkList = driver.find_elements_by_css_selector('td.ta_l>a')
		filename = driver.find_elements_by_css_selector('.area_header>header>h1>a>img')[0]
		filename = filename.get_attribute("alt")
		filepath = "pagelist/{0}.txt".format(filename)
		if os.path.isfile(filepath) == False:
			pageUrl = open(filepath, mode="at", encoding="utf-8")
			for link in linkList:
				pageUrl.write("{0}\n".format(link.get_attribute('href')))

		driver.quit()
		time.sleep(2)

		pageUrlFile = open(filepath)
		pageList = pageUrlFile.readlines()

		dirPath = "download/{0}".format(filename)
		try:
			if not (os.path.isdir(dirPath)):
				os.makedirs(os.path.join(dirPath))
		except OSError as e:
			print("{0} Failed to create directory!!!!!".format(dirPath))

		# chrome download folder option
		options = webdriver.ChromeOptions()
		options.add_experimental_option("prefs", {
			"download.default_directory": "{0}\\download\\{1}".format(os.getcwd(), filename),
			"download.prompt_for_download": False,
			"download.directory_upgrade": True,
			"safebrowsing_for_trusted_sources_enabled": False,
			"safebrowsing.enabled": False
		})
		downloadDriver = webdriver.Chrome(chromedriver, chrome_options=options)
		for page in pageList:
			try:
				page = page.rstrip("\n")
				downloadDriver.get(page)
				aTagList = WebDriverWait(downloadDriver, 2).until(selector_find)
				file_list = []
				for aTag in aTagList:
					if ".hwp" in aTag.text:
						file_list.append(aTag.get_attribute('href'))

				for file_url in file_list:
					downloadDriver.get(file_url)
					time.sleep(1.3)
			except:
				print('{0} error '.format(page))
				continue
		downloadDriver.quit()

schoolList= open('list.txt')
school = schoolList.readlines()
process_cnt = 5
division = len(school)/process_cnt
if( division != int(division)):
	process_cnt += 1
	division = int(division)

for i in range(0,process_cnt):
	if i != (process_cnt -1) :
		threading.Thread(target=selenium_crawler, args=([school[division*i:division*(i+1)]])).start()
	else:
		threading.Thread(target=selenium_crawler, args=([school[division * i:]])).start()

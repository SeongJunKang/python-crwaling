from selenium import webdriver
import time
import os

chromedriver = '../chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
schoolList = open('list.txt')
school = schoolList.readlines()
for url in school:
	url = "{0}&listCo=1500".format(url)
	driver.get(url)
	linkList = driver.find_elements_by_css_selector('td.ta_l>a')
	filename = driver.find_elements_by_css_selector('.area_header>header>h1>a>img')[0]
	filename = filename.get_attribute("alt")
	filepath = "pagelist/{0}.txt".format(filename)
	if os.path.isfile(filepath) == False:
		pageUrl = open(filepath,mode="at",encoding="utf-8")
		for link in linkList:
			pageUrl.write("{0}\n".format(link.get_attribute('href')))

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
		"download.default_directory": "{0}\\download\\{1}".format(os.getcwd(),filename),
		"download.prompt_for_download": False,
		"download.directory_upgrade": True,
		"safebrowsing_for_trusted_sources_enabled": False,
		"safebrowsing.enabled": False
	})
	downloadDriver = webdriver.Chrome(chromedriver,chrome_options=options)
	for page in pageList:
		try:
			downloadDriver.get(page)
			fileList = downloadDriver.find_elements_by_css_selector('.fileimg>li')
			for file in fileList:
				aTagList = file.find_elements_by_css_selector('a')
				for aTag in aTagList:
					if ".hwp" in aTag.text:
						aTag.click()
						time.sleep(1.2)
		except:
			continue
	downloadDriver.quit()
driver.quit()
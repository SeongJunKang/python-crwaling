from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import re
import os

# dir
dirPath = "../한식의 마음"
try:
	if not (os.path.isdir(dirPath)):
		os.makedirs(os.path.join(dirPath))
except OSError as e:
	print("{0} Failed to create directory!!!!!".format(dirPath))

chromedriver = '../../chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
url='http://www.kculture.or.kr/brd/board/601/L/menu/586?brdType=R&thisPage=1&bbIdx=11248&searchField=&searchText=&recordCnt=10'
while '#n' not in url:
	driver.get(url)
	mediaWrap = WebDriverWait(driver, 2).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, ".notice_table2")))
	next_tr = driver.find_elements_by_css_selector('table.prev_next_content tr')[1]
	next_url = next_tr.find_elements_by_css_selector('td a')[0].get_attribute('href')
	try:
		title = driver.find_elements_by_css_selector('.contentsTitle')[0].text
		title = re.sub(r"[\\|\/|\:|\*|\?|\"|\<|\>|\|]", '', title)
		xml_file = open('{0}\\{1}.xml'.format(dirPath, title), mode="wt", encoding="utf-8")

		info_agree = driver.find_elements_by_css_selector('.notice_table2')
		if len(info_agree) > 0:
			xml_file.write(info_agree[0].get_attribute('innerHTML'))
	except:
		print("Unexpected error:", sys.exc_info()[0])
		print('{0} error '.format(driver.current_url))
	finally:
		url = next_url
driver.quit()

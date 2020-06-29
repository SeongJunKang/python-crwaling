from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import re
import os

# dir
dirPath = "download"
try:
	if not (os.path.isdir(dirPath)):
		os.makedirs(os.path.join(dirPath))
except OSError as e:
	print("{0} Failed to create directory!!!!!".format(dirPath))

# chrome download folder option
donwload_loc = "{0}\\download".format(os.getcwd())
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
	"download.default_directory": donwload_loc,
	"download.prompt_for_download": False,
	"download.directory_upgrade": True,
	"safebrowsing_for_trusted_sources_enabled": False,
	"safebrowsing.enabled": False
})

chromedriver = '../chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
# 소식을 게시판 별로 첫번째 기사의 URL을 입력
url = 'http://www.k-heritage.tv/brd/board/256/L/CATEGORY/614/menu/253?brdType=R&thisPage=1&bbIdx=18597&searchField=&searchText='
while '#n' not in url:
	driver.get(url)
	mediaWrap = WebDriverWait(driver, 2).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, ".media_wrap")))
	next_url = driver.find_elements_by_css_selector('div.thumList>dl>dd>a')[0].get_attribute('href')
	try:
		title = driver.find_elements_by_css_selector('p.sub_tit2 em.sub_mode')[0].text
		title = re.sub(r"[\\|\/|\:|\*|\?|\"|\<|\>|\|]",'',title)
		xml_file = open('download\\{0}.xml'.format(title),mode="wt", encoding="utf-8")
		info_agree = driver.find_elements_by_css_selector('div.info_agree')
		type_cont = driver.find_elements_by_css_selector('.media_wrap .type_cont')
		card_cont_info = driver.find_elements_by_css_selector('.media_wrap .card_cont_info')
		if len(info_agree) > 0:
			xml_file.write(info_agree[0].get_attribute('innerHTML'))
		elif len(type_cont) > 0:
			xml_file.write(type_cont[0].get_attribute('innerHTML'))
		elif len(card_cont_info) > 0:
			xml_file.write(card_cont_info[0].get_attribute('innerHTML'))
	except:
		print("Unexpected error:", sys.exc_info()[0])
		print('{0} error '.format(driver.current_url))
	finally:
		url = next_url
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import sys
import time
import os

# directory 현재 경로에 download폴더 생성
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

# chrome driver 경로
chromedriver = '../chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver, chrome_options=options)

# 제일 맨처음 URL
# url = 'http://www.k-heritage.tv/brd/board/909/L/CATEGORY/911/menu/901?brdType=R&thisPage=1&bbIdx=20474&searchField=&searchText='
# 중간 URL
url = 'http://www.k-heritage.tv/brd/board/909/L/CATEGORY/911/menu/901?brdType=R&thisPage=1&bbIdx=17438&searchField=&searchText='
while '#n' not in url:
	#url 호출
	driver.get(url)
	# 해당 tag가 생성될 때 까지 기다림
	mediaWrap = WebDriverWait(driver, 2).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, ".media_wrap")))
	# 다음페이지 url 저장
	next_url = driver.find_elements_by_css_selector('div.thumList>dl>dd>a')[0].get_attribute('href')
	try:
		# hwp 파일이 있는경우 저장
		aTagList = driver.find_elements_by_css_selector("dl.b_file dd li a")
		file_list = []
		for aTag in aTagList:
			if ".hwp" in aTag.text:
				file_list.append(aTag.get_attribute('href'))

		for file_url in file_list:
			driver.get(file_url)
			time.sleep(1.3)

		# hwp 파일이 없으면 html 특정 태그를 xml로 저장
		if len(file_list) == 0:
			title = driver.find_elements_by_css_selector('p.sub_tit2 em.sub_mode')[0].text
			# 윈도우에서 파일명에 저장할 수 없는 문자 제거
			title = re.sub(r"[\\|\/|\:|\*|\?|\"|\<|\>|\|]",'',title)
			xml_file = open('download\\{0}.xml'.format(title),mode="wt", encoding="utf-8")
			xml_file.write(driver.find_elements_by_css_selector('div.type_cont')[0].get_attribute('innerHTML'))
	except IndexError:
		# 간혹 파일 다운로드 url이 오류가 발생하는 경우가 있음
		driver.get(url)
		mediaWrap = WebDriverWait(driver, 2).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, ".media_wrap")))
		title = driver.find_elements_by_css_selector('p.sub_tit2 em.sub_mode')[0].text
		title = re.sub(r"[\\|\/|\:|\*|\?|\"|\<|\>|\|]",'',title)
		xml_file = open('download\\{0}.xml'.format(title),mode="wt", encoding="utf-8")
		# 유형 확인
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

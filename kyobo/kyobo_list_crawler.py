from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
url = 'https://search.kyobobook.co.kr/web/search?vPstrKeyWord={0}&currentPage={1}'
# 검색어 등록
search_word_list = ['딥러닝', '머신러닝', '인공지능', '파이썬']

# 검색어로 나타난 목록 URL 다운로드하기
for word in search_word_list:
	driver.get(url.format(word, 1))
	search = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody#search_list tr")))
	totalpage = driver.find_element_by_css_selector('#totalpage').text
	for currentPage in range(1, int(totalpage)+1):
		driver.get(url.format(word, currentPage))
		tr_list = driver.find_elements_by_css_selector('.list_search_result tbody#search_list tr')
		f = open(word+".txt", mode="at", encoding="utf-8")
		for tr in tr_list:
			try:
				td = tr.find_element_by_css_selector('.detail')
				a_tag = td.find_element_by_css_selector('.title a')
				link = a_tag.get_attribute("href")
				if link:
					f.write(link+"\n")
			except:
				print("Unexpected error:", sys.exc_info()[0])
				print('{0} error '.format(driver.current_url))
driver.quit()

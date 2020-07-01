from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chromedriver = '../../chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
url = 'http://www.kculture.or.kr/brd/board/640/L/menu/641?brdType=L&thisPage={0}&rootCate=&searchField=&searchText=&recordCnt=300'
f = open("list.txt",mode="wt",encoding="utf-8")
for page in range(1, 5):
	driver.get(url.format(page))
	WebDriverWait(driver, 5).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, ".initial_search_content")))

	link_list = driver.find_elements_by_css_selector('.initial_btn a')
	for link in link_list:
		href = link.get_attribute('href')
		try:
			f.write("{0}\n".format(href))
		except:
			print("{0} ERROR\n".format(href))
driver.quit()

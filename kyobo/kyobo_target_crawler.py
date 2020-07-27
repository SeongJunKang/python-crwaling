from selenium import webdriver
import threading
import os

def crawling(filename):
	# 저장된 파일명으로 폴더 만들고
	try:
		if not (os.path.isdir(filename)):
			os.makedirs(os.path.join(filename))
	except OSError as e:
		print("{0} Failed to create directory!!!!!".format(filename))

	chromedriver = 'chromedriver.exe'
	driver = webdriver.Chrome(chromedriver)
	url_list = open(filename+'.txt', mode='rt', encoding='utf-8')
	lines = url_list.readlines()
	#저장된 URL에서 목차정보 가져오기
	for line in lines:
		line = line.rstrip("\n")
		if '&barcode=' not in line:
			continue
		try:
			barcode = line.split("&barcode=")[1].split("&")[0]
			driver.get(line)
			contents = driver.find_element_by_xpath(
				"//h2[@class='title_detail_basic' and contains(text(),'목차')]/following-sibling::div")
			xml_file = open('{0}\\{1}.xml'.format(filename, barcode), mode="wt", encoding="utf-8")
			xml_file.write(contents.get_attribute('innerHTML'))
		except:
			# 모든 페이지에 목차가 있는 것은 아니기 때문에 예외처리
			print('{0} error '.format(driver.current_url))
	driver.quit()


#검색어로 다운로드 받은 URL 파일명
target_list = ['딥러닝', '머신러닝', '인공지능', '파이썬']

for filename in target_list:
	threading.Thread(target=crawling, args=[filename]).start()

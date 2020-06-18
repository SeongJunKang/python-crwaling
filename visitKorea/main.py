from selenium import webdriver
import os

f = open('list.txt')
lines = f.readlines()
chromedriver = 'chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
for line in lines:
	line = line.rstrip("\n")
	try:
		fileExist = os.path.isfile("download/{0}.xml".format(line));
		if fileExist == False :
			print(line)
			driver.get('https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid={0}'.format(line))
			contents_list = driver.find_elements_by_css_selector('div#contents')
			download = open("download/{0}.xml".format(line),mode="at",encoding="utf-8");
			for contents in contents_list:
				download.write(contents.get_attribute("innerHTML"))
	except :
		print('{0}에서 에러가 발생했습니다.'.format(line));
print("VisitKorea Crawling Finished")
driver.quit()
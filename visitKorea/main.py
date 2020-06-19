from selenium import webdriver

f = open('list.txt')
lines = f.readlines()
chromedriver = 'chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
for line in lines:
	line = line.rstrip("\n")
	try:
		param = line.split(',', maxsplit=2)
		if int(param[1]) == 30000:
			continue
		elif int(param[1]) > 10000:
			driver.get('https://korean.visitkorea.or.kr/detail/rem_detail.do?cotid={0}'.format(param[0]))
		else:
			driver.get('https://korean.visitkorea.or.kr/detail/ms_detail.do?cotid={0}'.format(param[0]))
		contents_list = driver.find_elements_by_css_selector('div#contents')
		download = open("download/{0}.xml".format(param[0]),mode="wt",encoding="utf-8");
		for contents in contents_list:
			download.write(contents.get_attribute("innerHTML"))
	except :
		print('{0}에서 에러가 발생했습니다.'.format(line));
print("VisitKorea Crawling Finished")
driver.quit()
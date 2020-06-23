from selenium import webdriver

chromedriver = 'chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
urlFormat = "https://www.cdc.go.kr/board/board.es?mid=a20501000000&bid=0015&nPage={0}"
f = open("list.txt",mode="wt",encoding="utf-8")
for page in range(1, 404):
	driver.get(urlFormat.format(page))
	linkList = driver.find_elements_by_css_selector('#listView .title a')
	for link in linkList:
		href = link.get_attribute("href")
		try:
			f.write("{0}\n".format(href))
		except:
			print("{0} ERROR\n".format(href))

driver.quit()
from selenium import webdriver
import time

chromedriver = 'chromedriver/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
urlFormat = "http://www.cdc.go.kr/npt/biz/npp/portal/nppIssueIcdMain.do?issueIcdSn=&totalRowCount=&schType=0&schTxt=&schRow={0}&pageIndex=1".format(600)
driver.get(urlFormat)

time.sleep(2)

f = open("list.txt",mode="wt",encoding="utf-8");
linkList = driver.find_elements_by_css_selector('a.btn-list')
for link in linkList:
	href = link.get_attribute("href")
	number = href.replace("javascript:fn_view('","").replace("');","")
	try:
		f.write("{0}\n".format(number))
	except:
		print("{0}\n".format(number))

driver.quit()
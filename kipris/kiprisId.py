from selenium import webdriver
import os
import re
import threading
'''
1. <doc></doc>형식으로 저장되야함.
2. &nbsp;를 공백으로 수정
3. iframe 안의 tag를 호출해야함
'''
def selenium_crawler(list : list):
	chromedriver = '../chromedriver.exe'
	driver = webdriver.Chrome(chromedriver)
	dir = "C:/Users/crawling/"
	url = "http://kpat.kipris.or.kr/kpat/biblioa.do?method=biblioFrame&applno={0}"
	for id in list:
		try:
			id = id.rstrip("\n")
			folder = id[:6]
			filePath = dir + folder + "/" + id + ".xml"
			if os.path.isfile(filePath) == False:
				driver.get(url.format(id))
				try:
					title = driver.find_element_by_css_selector("#divBiblioTop h1.title")
					titleString = "<h1 class='title'>\n"
					titleString += title.get_attribute("innerHTML")
					titleString += "\n</h1>"
				except Exception as ex2:
					titleString = ""
				iframe = driver.switch_to.frame("ifrmDetailArea")
				con_scroll = driver.find_element_by_css_selector("div.con_scroll")
				content = "<doc>\n"
				content += titleString + "\n" + con_scroll.get_attribute("innerHTML")
				content += "\n</doc>"

				content = re.sub("<img .*?[^>]>", "", content)
				content = re.sub("<iframe .*?</iframe>", "", content)
				content = re.sub("<br>", "<br/>", content)
				content = re.sub("&nbsp;", " ", content)

				if not (os.path.isdir(dir + folder)):
					os.makedirs(os.path.join(dir + folder))
				write = open(dir + folder + "/" + id + ".xml", mode="wt", encoding="utf-8")
				write.write(content)
				write.close()
		except Exception as ex:
			print("error", id, ex)

	driver.quit()



dir = "C:/Users/crawling/"
file = open(dir+"list.txt", mode="rt", encoding="utf-8")
list = file.readlines()
process_cnt = 10
division = len(list)/process_cnt
if division != int(division):
	process_cnt += 1
	division = int(division)

for i in range(0, process_cnt):
	if i != (process_cnt - 1):
		threading.Thread(target=selenium_crawler, args=([list[division*i:division*(i+1)]])).start()
	else:
		threading.Thread(target=selenium_crawler, args=([list[division * i:]])).start()

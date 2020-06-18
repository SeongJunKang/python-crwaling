import requests
import math

urlFormat = "https://korean.visitkorea.or.kr/call?cmd=CONTENT_MASTER_LIST_VIEW&areaCode=All&sigunguCode=All&tagId=All&locationx=0&locationy=0&sortkind=1&page={0}&cnt={1}"
json = requests.get(urlFormat.format(1,1)).json()

body = json["body"]
totalCount = body["totalCount"]
f = open("list.txt",mode="at",encoding="utf-8");

totalPage = math.ceil(totalCount / 1000)
for page in range(1,totalPage+1):
	json = requests.get(urlFormat.format(page, 1000)).json()
	body = json["body"]
	result = body["result"]
	for item in result:
		f.write("{0}\n".format(item["cotId"]))
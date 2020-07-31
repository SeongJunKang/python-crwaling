# 특정 웹사이트 크롤러 

### 특정 웹사이트를 크롤링해야하는 상황이 생겨서 크롤링 소스를 저장

#### 크롤링을 진행했던 사이트 목록

- [대한민국 구석구석](https://korean.visitkorea.or.kr/)
- [질병관리본부(감염병 포털)- 감염병 보도자료 PDF 파일](http://www.cdc.go.kr/npt/biz/npp/portal/nppIssueIcdMain.do)
- [질병관리본부 - 보도자료](https://www.cdc.go.kr/board/board.es?mid=a20501000000&bid=0015)
- [문화유산채널 - 이야기 4종류](http://www.k-heritage.tv/main/heritage)
- [한국음식문화 - 한식문화사전, 한식문화공감 크롤링](http://www.kculture.or.kr/main/hansikculture)
- [교보문고-목록, 목차 크롤링 Using Keyword](http://www.kyobobook.co.kr/index.laf)



## 버전정보
### IDE
- PyCharm Community Edition 2020.1

### version
- python 3.6.7
- chromedriver

## Libraries
### pip install Libraries
- requests
- bs4
- selenium

### 병렬처리를 위한 Libraries
- threading

## 크롤링 예제
### 1. 정적사이트(bs4)
- ajax를 호출하지 않는 정적 사이트의 경우는 requests, bs4로 해결가능합니다.
- (선행) 아래의 라이브러리를 설치해야 사용가능합니다. :
-- pip install requests
-- pip install bs4

```
import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
# response = requests.get(url) # get request call
# response = requests.post(url) # post request call

headers = {'Content-Type': 'application/json; charset=utf-8'} 
cookies = {'session_id': 'sessionIdValue'} 
req.add_header('User-Agent', 'Mozilla/5.0')
response = requests.get(url, headers=headers, cookies=cookies) # request call incluing headers, cokkies

if response.ok: # 해당 데이터를 정상적으로 가져왔으면 True 아니면 False 를 리턴
  html = response.text # response로 가져온 Html text
  print(html)
  soup = BeautifulSoup(html,'html.parser')  # html을 bs4로 파싱
  logo = soup.select_one('.logo_naver') # 'logo_naver' class를 가지는 태그 가져옴  
  print(logo)
  print(logo.attrs)
  for attr in logo.attrs:
    print(attr)

```


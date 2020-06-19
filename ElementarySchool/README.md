# 초등학교 가정통신문 한글파일 크롤링

- python version : 3.6.7

- list.txt 파일에 해당하는 URL만 적용됩니다.(doamin이 busanedu만 해당)<br>

- selenium을 통해 가정통신문의 목록을 가져옵니다.<br>
- 가져온 가정통신문의 목록을 파일로 저장하고, 저장한 파일을 불러옵니다.<br>
- 불러온 파일(가정통신문의 목록)을 하나씩 호출하여 가정통신문 한글파일을 다운로드합니다.<br>

- chromedriver를 이용했습니다. chromedriver.exe가 있어야 동작합니다. (windows10)<br>
- [크롬 웹드라이버 다운로드](https://chromedriver.chromium.org/downloads)
# [질병관리본부(KCDC) 보도자료](https://www.cdc.go.kr/board/board.es?mid=a20501000000&bid=0015&list_no=367586&act=view) HWP다운로드

## version
- python version : 3.6.7
- selenium (chrome Driver)

## contents
- 질병관리본부 보도자료 목록을 다운로드 받아 list.txt로 저장합니다.<br>
- 저장한 목록(list.txt)를 열어서 한줄마다 보도자료 상세화면으로 이동한다.<br>
- 다운로드 목록에 있는 hwp 파일을 확인하고 .hwp파일만 다운로드한다.<br>
- hwp 파일이 없는 페이지는 건너뜁니다.<br>

## etc
- chromedriver를 이용했습니다. chromedriver.exe가 있어야 동작합니다. (windows10)<br>
- [크롬 웹드라이버 다운로드](https://chromedriver.chromium.org/downloads
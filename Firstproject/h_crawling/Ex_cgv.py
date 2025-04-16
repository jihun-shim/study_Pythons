import requests
from bs4 import BeautifulSoup

# CGV 사이트에서 현재 영화차트 3위의 제목들을 추출

#requests 라이브러리의 get메소드를 사용하여 접속하기
r = requests.get("http://www.cgv.co.kr/movies/?lt=1&ft=0")
c = r.content
#print(c)

# BeautifulSoup의 html.parser 기능을 이용하여 파싱이 쉽게 될 수 있도록
html = BeautifulSoup(c,"html.parser")
#print(html)

ol = html.find('ol')  # <ol> 태그 찾음

li = ol.find_all("li") # ol내의 <li>태그들을 찾음 (각 영화의 정보들은 리스트의 요소)
print(li)

for l in li:
    div = l.find('div',{"class":"box-contents"})
    title = div.find("strong").text # div태그의 자손중 <strong>태그의 내용
    print(title)

# 벅스뮤직 실시간 차트 곡명/가수명 추출
r = requests.get("https://music.bugs.co.kr/chart")
c = r.content
#print(c)

"""
import requests
from bs4 import BeautifulSoup

url = requests.get("https://music.bugs.co.kr/chart")
content = url.content

html = BeautifulSoup(content, "html.parser")

tbody = html.find("tbody")
tr = tbody.find_all("tr")

for t in tr[:3]:
    th = t.find("th")
    td = t.find("td", {"class": "left"})
    p1 = th.find("p").text
    p2 = td.find("p").text
    print("{} - {}".format(p1, p2))
"""
import requests
from bs4 import BeautifulSoup

url = requests.get("https://music.bugs.co.kr/chart")
content = url.content

html = BeautifulSoup(content, "html.parser")

tbody = html.find("tbody")

li = tbody.find_all("th")
td = tbody.find_all("p", "artist")

for p in range(len(li)):
    title = li[p].find("p", {"class": "title"})
    tt = title.find("a").text
    print(tt, td[p].find("a").text, sep=" | ")
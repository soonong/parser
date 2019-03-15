import requests
from bs4 import BeautifulSoup

url = "http://www.keca.or.kr/ecic/ad/ad0101.do?menuCd=6047&currentPageNo=2&license=&gubun=page&sido=&hoeyn=&searchSido=&searchSigungu=&searchGubun=company&searchText=&CSRFToken=9e5d83eb-10bb-4fb5-8da4-60733f94b776"
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c,"html.parser")

list = soup.find("div",{"class":"list"})
tbody = list.find("tbody")
trs = tbody.findAll("tr")

for tr in trs :
    tds = tr.findAll("td")[1].find("a")['href']
    print(tds)
    

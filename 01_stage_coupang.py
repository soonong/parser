import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import pandas as pd

def crawl(pageNo):
    encText = urllib.parse.quote(keyword)
    url = "https://www.coupang.com/np/search?q={}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=".format(encText, pageNo)
    data = requests.get(url)
    result = data.content
    return result

def get_product(li):        
    name = li.find("div", {"class": "name"}).text
    price = li.find("strong", {"class": "price-value"}).text.replace(",", "")
    rate = li.find("span", {"class": "rating-total-count"}).text.replace("(", "").replace(")", "")
    return {"name": name, "price": price, "count": rate}


def parse(pageString):
    bsObj = BeautifulSoup(pageString,"html.parser")
    seart_result = bsObj.find("div",{"class":"search-content"})
    ul = seart_result.find("ul",{"class":"search-product-list"})
    lis = ul.findAll("li",{"class":"search-product"})

    result = []
    for li in lis:
        try :
            product = get_product(li)
            result.append(product)
        except :
            print("error")

    return result


keyword = "신라면"
products = []
for pageNo in range(1,10):                 # 1. 왜 여기서 범위를 3이상을 하면 되고,  2나 1 하면 안되는지 궁금합니다.
    pageString = crawl(pageNo)
    ddd=parse(pageString)
    products = products + ddd


file = open("./coupang_list","w+")
file.write(json.dumps(products))

df = pd.read_json("./coupang_list")
print(df)
df.to_excel('noodle.xlsx', sheet_name='coupang')


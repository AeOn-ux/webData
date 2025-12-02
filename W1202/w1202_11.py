import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/index"
# selenium 함수 호출

# 파일 불러오기
with open("webtoon_browser.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
# ul = soup.find("ul",{"id":"menu"})
# lis = ul.find_all("li")
# print(lis[3].text.strip())


# for li in lis:
#     print(li.a.text.strip())


# 실시간 인기 웹툰 -------------------------------------------------------------
asideDiv = soup.find("div",{"class":"Aside__aside_wrap--iF5ju"})
# 실시간 인기 웹툰 - wraps[0]
wraps = asideDiv.find_all("div",{"class":"component_wrap"})
print(wraps[0].find("h2",{"class":"ComponentHead__title--TjYVo"}).text.strip())

ul = soup.find("ul",{"class":"AsideList__content_list--FXDvm"})
lis = ul.find_all("li")
# print(lis[0].text.strip())
lis2 = ul.find_all("span")
print(lis[1].text.strip())
lis3 = ul.find_all("a")
print(lis[2].text.strip())

# #실시간 인기 웹툰 리스트-----------------------------------------------------------
# for i in range(5):
#     print(lis[i].find("strong",{"class":"AsideList__ranking--sNPZy"}).text.strip())
#     print(lis[i].find("span",{"class":"ContentTitle__title--e3qXt"}).text.strip())
#     print(lis[i].find("a",{"class":"ContentAuthor__author--CTAAP"}).text.strip())
#     print("-"*50)
#-------------------------------------------------------------

# 실시간 신작 랭킹--------------------------------------------------------------------
# asideDiv = soup.find("div",{"class":"Aside__aside_wrap--iF5ju"})
# wraps = asideDiv.find_all("div",{"class":"component_wrap"})
# print(wraps[1].find("h2",{"class":"ComponentHead__title--TjYVo"}).text.strip())

# lis = wraps[1].find_all("li")
# for i in range(5):
   
#     print(lis[i].find("strong",{"class":"AsideList__ranking--sNPZy"}).text.strip())
#     print(lis[i].find("span",{"class":"text"}).text.strip())
#     print(lis[i].find("a",{"class":"ContentAuthor__author--CTAAP"}).text.strip())
#     print("-"*50)

# asideDiv = soup.find("nav",{"class":"GlobalNavigationBar__lnb_list--bwu26"})
# wraps = asideDiv.find_all("div",{"class":"GlobalNavigationBar__item--F7tIS"})
# print(wraps[3].find("h2",{"class":"ComponentHead__title--TjYVo"}))
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
# url ="https://tabelog.com/tw/rstLst/lunch/"
# response = urlopen(url)
# html = BeautifulSoup(response)
# # print(html)
p = 1
while True:
    r1 = requests.get(f"https://tabelog.com/tw/rstLst/{p}/?LstRev=1&RdoCosTp=1&SrtT=rtl")
    print("現在第幾頁",p)
    soup  = BeautifulSoup(r1.text,"html.parser")
    # for r2 in soup.find_all("li",{"class":"list-rst"}):
    #     for r3 in r2.find("p",{"class":"list-rst__name"}):
    #         print(r3.text.split())
    # finb_all 出來的是一個list
    for r2 in soup.find_all("li",class_="list-rst"): # li清單
        r3 = r2.find("small",class_="list-rst__name-ja") # small 字較小
        r4 = r2.find("a",class_="list-rst__name-main")
        r5 = r2.find("b", class_="c-rating__val")# b 粗體
        # 萃取紙條(.text)  萃取特徵([特徵])
        print(r5.text,r3.text,r4.text,r4["href"])
    
    p = p+1




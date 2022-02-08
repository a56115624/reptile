from urllib import response
from urllib.request import urlopen,urlretrieve
import json
import os
for m in range(12):
    url  = f"https://www.google.com/doodles/json/2021/{m+1}?hl=zh-TW"

    response = urlopen(url)

    doodles = json.load(response)
    # print(doodles)
    for i in doodles:
        url = "https:"+i["url"]
        # print(url)
        response = urlopen(url)
        img = response.read()
        # print(url.split("/")[-1])\

        # 請電腦創建資料夾
        # 案月份存檔
        dir = "doodles/"+str(m+1)+"/"
        if not os.path.exists(dir): # 檢查如果沒有dir
            os.makedirs(dir)# 創建資料夾
        finalname = dir+url.split("/")[-1]



        #標準儲存檔案
        # f = open(finalname,"wb")
        # f.write(img)
        # f.close()
        urlretrieve(url,finalname)# 直接儲存檔案的方法
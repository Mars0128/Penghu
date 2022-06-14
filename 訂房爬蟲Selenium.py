#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium.webdriver.support import expected_conditions as EC #網站是否已讀取完畢
from selenium import webdriver
import time
import openpyxl as op
import random
from selenium.webdriver import Chrome


# wb = op.Workbook("訂房網站.xlsx") #開啟新的工作簿
wb = op.load_workbook("訂房網站.xlsx")
ws = wb.active
# ws.append(["日期","飯店名稱","類型","地區","評分","價錢","訂房網站"])
# wb.save("訂房網站.xlsx")


driver=webdriver.Chrome("C:\\Users\\hsu\\chromedriver.exe",options=option)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
    "source":"""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
    })
    """
})

data = "https://www.trivago.com.tw/zh-Hant-TW/srl/%E9%A3%AF%E5%BA%97-%E6%BE%8E%E6%B9%96-%E5%8F%B0%E7%81%A3?search=200-389188;dr-20220501-20220502;rc-1-2"
driver.get(data)


for y in range(20220526,20220531):
    for x in range(1,6):
        data = "https://www.trivago.com.tw/zh-Hant-TW/lm/%E9%A3%AF%E5%BA%97-%E6%BE%8E%E6%B9%96-%E5%8F%B0%E7%81%A3?search=200-389188;dr-"+str(y)+"-"+str(y+1)+";pa-"+str(x)+";rc-1-2"
        driver.get(data)
        time.sleep(10)
        username=driver.find_elements_by_css_selector("li")
        a7=f"{y}-{y+1}"
        w=[]
        g=[]
        n=[]
        t=[]
        type_=["飯店","青年旅館","旅館","民宿","整間房屋/公寓"]
        for i in username:
            w.append(i.text)
        for i in range(len(w)):
            if "馬公市" in w[i]:
                g=[]
                e=w[i].replace(" ","").split("\n")
                for i in range(5):
                    if type_[i] in e:
                        n=e[e.index(type_[i])-1]
                        t=type_[i]
                        a5=n
                        a6=t
                        n=[]
                        t=[]
                a1=e[e.index("馬公市")]
                a2=e[e.index("馬公市")+1]
                a3=e[-2]
                a4=e[-1]
                ws.append([a7,a5,a6,a1,a2,a3,a4])
            elif "湖西鄉" in w[i]:     
                g=[]
                e=w[i].replace(" ","").split("\n")
                for i in range(5):
                    if type_[i] in e:
                        n=e[e.index(type_[i])-1]
                        t=type_[i]
                        a5=n
                        a6=t
                        n=[]
                        t=[]
                a1=e[e.index("湖西鄉")]
                a2=e[e.index("湖西鄉")+1]
                a3=e[-2]
                a4=e[-1]
                ws.append([a7,a5,a6,a1,a2,a3,a4])
            elif "白沙鄉" in w[i]:     
                g=[]
                e=w[i].replace(" ","").split("\n")
                for i in range(5):
                    if type_[i] in e:
                        n=e[e.index(type_[i])-1]
                        t=type_[i]
                        a5=n
                        a6=t
                        n=[]
                        t=[]            
                a1=e[e.index("白沙鄉")]
                a2=e[e.index("白沙鄉")+1]
                a3=e[-2]
                a4=e[-1]
                ws.append([a7,a5,a6,a1,a2,a3,a4])
            elif "七美鄉" in w[i]:     
                g=[]
                e=w[i].replace(" ","").split("\n")
                for i in range(5):
                    if type_[i] in e:
                        n=e[e.index(type_[i])-1]
                        t=type_[i]
                        a5=n
                        a6=t
                        n=[]
                        t=[]
                a1=e[e.index("七美鄉")]
                a2=e[e.index("七美鄉")+1]
                a3=e[-2]
                a4=e[-1]
                ws.append([a7,a5,a6,a1,a2,a3,a4])
            elif "西嶼鄉" in w[i]:     
                g=[]
                e=w[i].replace(" ","").split("\n")
                for i in range(5):
                    if type_[i] in e:
                        n=e[e.index(type_[i])-1]
                        t=type_[i]
                        a5=n
                        a6=t
                        n=[]
                        t=[]
                a1=e[e.index("西嶼鄉")]
                a2=e[e.index("西嶼鄉")+1]
                a3=e[-2]
                a4=e[-1]
                ws.append([a7,a5,a6,a1,a2,a3,a4])
        print(f"{a7},第{x}頁")
        print("---------------")      
        wb.save("訂房網站.xlsx")
        time.sleep(3)
    time.sleep(15)    


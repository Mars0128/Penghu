#!/usr/bin/env python
# coding: utf-8

# In[229]:


from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import openpyxl as op
import pymongo
import certifi

client = pymongo.MongoClient("mongodb+srv://test2:puqKxV7PsTl9yx3r@cluster0.jgt9o.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())

db = client.trivago
col = db.roomlist
def roomlist():
    text=tk.Text(tab2, height = 20, width = 75,bg = "#e6e6e6",font =("Courier", 15)) 
    text.place(x = 50, y = 90)
    t = int(entry0.get())
    data = {'價錢': {'$lt': t},'類型':var.get(),'日期':var1.get()}
    mydata = col.find(data)
    if var2.get() == "從小到大":
        mydata = mydata.sort("價錢",pymongo.ASCENDING)        
        for result2 in mydata:       
            strlist = []
            x = result2["飯店名稱"]
            f = result2["價錢"]
            o = result2["類型"]
            g = result2["訂房網站"]
            h = result2["平均價格"]
            i = result2["是否比較便宜"]
            j = result2["價差"]
            k = result2["倍率"]
            d = result2["地區"]
            p = result2["日期"]
            u = result2["評分"]
            strlist.append(f"{x:<20}\n訂房網站:{g:<15} 價錢:${f:<6} 平均價格:${h:<6} 價差:${j:<6} 評分:{u:<4}\n")
            text.insert("insert",'\n'.join(strlist))
            text.insert("insert","\n")


    elif var2.get() == "從大到小":
        mydata = mydata.sort("價錢",pymongo.DESCENDING)
        for result2 in mydata:
            strlist = []
            x = result2["飯店名稱"]
            f = result2["價錢"]
            o = result2["類型"]
            g = result2["訂房網站"]
            h = result2["平均價格"]
            i = result2["是否比較便宜"]
            j = result2["價差"]
            k = result2["倍率"]
            p = result2["日期"]
            d = result2["地區"]
            u = result2["評分"]
            strlist.append(f"{x:<20}\n訂房網站:{g:<15} 價錢:${f:<6} 平均價格:${h:<6} 價差:${j:<6} 評分:{u:<4}\n")   
            text.insert("insert",'\n'.join(strlist))
            text.insert("insert","\n")


    elif var2.get() == "從高到低":
        mydata = mydata.sort("評分",pymongo.DESCENDING)
        for result2 in mydata:
            strlist = []
            x = result2["飯店名稱"]
            f = result2["價錢"]
            o = result2["類型"]
            g = result2["訂房網站"]
            h = result2["平均價格"]
            i = result2["是否比較便宜"]
            j = result2["價差"]
            k = result2["倍率"]
            d = result2["地區"]
            p = result2["日期"]
            u = result2["評分"]
            strlist.append(f"{x:<20}\n訂房網站:{g:<15} 價錢:${f:<6} 平均價格:${h:<6} 價差:${j:<6} 評分:{u:<4}\n")    

            text.insert("insert",'\n'.join(strlist))
            text.insert("insert","\n")


    elif var2.get() == "從低到高":
        mydata = mydata.sort("評分",pymongo.ASCENDING)
        for result2 in mydata:
            strlist = []
            x = result2["飯店名稱"]
            f = result2["價錢"]
            o = result2["類型"]
            g = result2["訂房網站"]
            h = result2["平均價格"]
            i = result2["是否比較便宜"]
            j = result2["價差"]
            k = result2["倍率"]
            p = result2["日期"]
            d = result2["地區"]
            u = result2["評分"]
            strlist.append(f"{x:<20}\n訂房網站:{g:<15} 價錢:${f:<6} 平均價格:${h:<6} 價差:${j:<6} 評分:{u:<4}\n")
            text.insert("insert",'\n'.join(strlist))
            text.insert("insert","\n")


    elif var2.get() == "從多到少":
        mydata = mydata.sort("價差",pymongo.ASCENDING)
        for result2 in mydata:
            strlist = []
            x = result2["飯店名稱"]
            f = result2["價錢"]
            o = result2["類型"]
            g = result2["訂房網站"]
            h = result2["平均價格"]
            d = result2["地區"]
            j = result2["價差"]
            k = result2["倍率"]
            p = result2["日期"]
            u = result2["評分"]
            strlist.append(f"{x:<20}\n訂房網站:{g:<15} 價錢:${f:<6} 平均價格:${h:<6} 價差:${j:<6} 評分:{u:<4}\n")
            text.insert("insert",'\n'.join(strlist))
            text.insert("insert","\n")


    elif var2.get() == "從少到多":
        mydata = mydata.sort("價差",pymongo.DESCENDING)
        for result2 in mydata:
            strlist = []
            x = result2["飯店名稱"]
            f = result2["價錢"]
            g = result2["訂房網站"]
            h = result2["平均價格"]
            i = result2["是否比較便宜"]
            j = result2["價差"]
            k = result2["倍率"]
            p = result2["日期"]
            u = result2["評分"]
            strlist.append(f"{x:<20}\n訂房網站:{g:<15} 價錢:${f:<6} 平均價格:${h:<6} 價差:${j:<6} 評分:{u:<4}\n")
            text.insert("insert",'\n'.join(strlist))
            text.insert("insert","\n")

def close_window():
    root.destroy()         

root=Tk()
root.title("訂房網站查詢")
root.geometry("1000x575")
root.configure(bg = "#ffffff")

tab=ttk.Notebook()
tab.place(x = 0, y = 0, width=1000 ,height=575)

tab1=Frame(tab)
tab1.place(x = 0, y = 0)
tab.add(tab1,text='訂房小幫手')

canvas = Canvas(
    tab1,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
img0 = PhotoImage(file = f"img0.png")
optionList = ['類型','飯店','整間房屋/公寓','民宿','旅館','青年旅館']
var = tk.StringVar()
var.set(optionList[0])
myoptionmenu = tk.OptionMenu(tab1, var, *optionList)
myoptionmenu.config(bg = "#e6e6e6",font =("Courier", 20))
myoptionmenu.place(x =700 , y = 110)


optionList = ['活動日期','04/25 星期一','04/28 星期四','05/02 星期一','05/05 星期四','05/09 星期一','05/12 星期四','05/16 星期一',
            '05/19 星期四','05/21 星期六','05/23 星期一','05/26 星期四','05/28 星期六','05/30 星期一','06/02 星期四','06/06 星期一',
            '06/09 星期四','06/11 星期六','06/13 星期一','06/16 星期四','06/20 星期一','06/23 星期四','06/25 星期六','06/27 星期一','06/30 星期四']
var1 = tk.StringVar()
var1.set(optionList[0])
myoptionmenu = tk.OptionMenu(tab1, var1, *optionList)
myoptionmenu.config(bg = "#e6e6e6",font =("Courier", 20))
myoptionmenu.place(x =700 , y = 200)

optionList = ['排序','"價錢排序"','從小到大','從大到小','---------','"評分排序"','從高到低','從低到高','---------','"折價排序"','從多到少','從少到多',]
var2 = tk.StringVar()
var2.set(optionList[0])
myoptionmenu = tk.OptionMenu(tab1, var2, *optionList)
myoptionmenu.config(bg = "#e6e6e6",font =("Courier", 20))
myoptionmenu.place(x =700 , y = 290)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 287.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    807.5, 396.5,
    image = entry0_img)

entry0 = Entry(tab1,
    bd = 0,
    bg = "#e6e6e6",
    font =("Courier", 20),
    highlightthickness = 0)

entry0.place(
    x = 713.5, y = 370,
    width = 188.0,
    height = 57)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(tab1,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command= close_window,
    relief = "flat"
        )

b0.place(
    x = 708, y = 454,
    width = 200,
    height = 89)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(tab1,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command=roomlist,
    relief = "flat")

b1.place(
    x = 500, y = 454,
    width = 203,
    height = 89)




tab2=Frame(tab)
tab2.place(x = 0, y = 0)
tab.add(tab2,text='搜尋結果')

Text=Text(tab2,width=500,height=100)
Text.place(x=10,y=100)
canvas2 = Canvas(
    tab2,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas2.place(x = 0, y = 0)


background_img2 = PhotoImage(file = f"background1.png")
background2 = canvas2.create_image(
    500.0, 287.5,
    image=background_img2)



root.resizable(False, False)
root.mainloop()


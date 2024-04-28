from tkinter import *
from tkinter import  ttk
import requests
win = Tk()
win.title("Weather app")
win.config(bg="blue")
win.geometry("550x550")


def data_get():
    city = city_name.get()
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=fec4c0949e73d41f75064292b4fe5d02").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

name_label = Label(win,text="weather app",font=("Times new Roman",35,"bold"))
name_label.place(x=30,y=40,height=50,width=400)
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
city_name=StringVar()
com = ttk.Combobox(win, values=list_name, font=("Times new Roman", 35, "bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


w_label = Label(win,text="weather climate",font=("Times new Roman", 20))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="",font=("Times new Roman", 20))
w_label1.place(x=250,y=260,height=50,width=210)

wd_label = Label(win,text="weather Description",font=("Times new Roman", 17))
wd_label.place(x=25,y=330,height=50,width=210)

wd_label1 = Label(win,text="",font=("Times new Roman", 17))
wd_label1.place(x=250,y=330,height=50,width=210)


temp_label = Label(win,text="Temperature",font=("Times new Roman", 20))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text="",font=("Times new Roman", 20))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label = Label(win,text="Pressure",font=("Times new Roman", 20))
per_label.place(x=25,y=470,height=50,width=210)

per_label1 = Label(win,text="",font=("Times new Roman", 20))
per_label1.place(x=250,y=470,height=50,width=210)

btn = Button(win,text="Click",font=("Times new Roman",20,"bold"),command=data_get)
btn.place(x=200,y=190,height=50,width=100)
win.mainloop()
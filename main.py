import tkinter as tk
from tkinter import ttk
from tkinter import * 

from PIL import ImageTk, Image
import os
import requests
from io import BytesIO


img_url1 = "https://media.discordapp.net/attachments/644219379827081228/1057038430783143936/ordek.png?width=72&height=72"
response1 = requests.get(img_url1)
img_data1 = response1.content

img_url2 = "https://cdn.discordapp.com/attachments/644219379827081228/1058103218233692181/madduck-removebg_4.png"
response2 = requests.get(img_url2)
img_data2 = response2.content



# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = tInputBir.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = tInputIki.get()
	return userInput



root = Tk()
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)

# This is the section of code which creates the main window
root.geometry('500x150')
root.configure(background='#2F4F4F')
root.title('ORDEK Hesaplayici')

img1 = ImageTk.PhotoImage(Image.open(BytesIO(img_data1)))
ordek = tk.Label(root, image=img1, bg='#2F4F4F')
ordek.place(x=182,y=75)

madduckIMG = ImageTk.PhotoImage(Image.open(BytesIO(img_data2)))
madduck = tk.Label(root, image=madduckIMG, bg='#2F4F4F')


etobuto = tk.Label(root, text='EtoButo#0001', bg='#2F4F4F', font=('helvetica', 9, 'normal'))
etobuto.place(x=18,y=18)


yazi1 = tk.Label(root, text='Steam Fiyati', bg='#2F4F4F', font=('helvetica', 13, 'normal', 'underline'))
yazi2 = tk.Label(root, text='% Yuzdesi', bg='#2F4F4F', font=('helvetica', 13, 'normal', 'underline'))
yazi3 = tk.Label(root, text='Nakit Fiyati:', bg='#2F4F4F', font=('helvetica', 13, 'normal', 'underline'))

yazi1.place(x=110, y=17)
yazi2.place(x=230, y=17)
yazi3.place(x=350,y=17)


# This is the section of code which creates a text input box
tInputBir=Entry(root,width=7, font=('helvetica', 12, 'bold'))
tInputBir.place(x=125, y=60)


# This is the section of code which creates a text input box
tInputIki=Entry(root,width=7, font=('helvetica', 12, 'bold'))
tInputIki.place(x=240, y=61)


# This is the section of code which creates the a label
TL_Yazisi = tk.Label(root, text='', bg='#2F4F4F', font=('helvetica', 12, 'bold'))
TL_Yazisi.place(x=400, y=105)

tum_fiyat = tk.Label(root, text='Tum Fiyat: ', bg='#2F4F4F', font=('helvetica', 9, 'bold'), anchor="n")
komisyon = tk.Label(root, text='%15 Komisyon: ', bg='#2F4F4F', font=('helvetica', 9, 'bold'), anchor="n")
son_fiyat = tk.Label(root, text='Son Fiyat: ', bg='#2F4F4F', font=('helvetica', 12, 'bold'), anchor="n")

tum_fiyat.place(x=328,y=50)
komisyon.place(x=320,y=75)
son_fiyat.place(x=320,y=105)

def clrText():
    tInputBir.delete(0, END)
    tInputIki.delete(0, END)
    tum_fiyat.config(text=f"Tum Fiyat: ")
    komisyon.config(text=f"%15 Komisyon: ")
    son_fiyat.config(text=f"Son Fiyat: ")
    madduck.place_forget()

def change_text():
    madduck.place_forget()
    try:
        sayi1 = int(tInputBir.get())
        sayi2 = int(tInputIki.get())

        tlDegeri = sayi1*sayi2/100
        tlDegeriSon = ((sayi1*sayi2/100)*85)/100
        tlKomisyon15 = ((sayi1*sayi2/100)*15)/100

        tlDegeri = str("{:.2f}".format(tlDegeri))
        tlDegeriSon = str("{:.2f}".format(tlDegeriSon))
        tlKomisyon15 = str("{:.2f}".format(tlKomisyon15))

        #TL_Yazisi.config(text=f"{tlDegeri} TL")
        tum_fiyat.config(text=f"Tum Fiyat: {tlDegeri} TL")
        komisyon.config(text=f"%15 Komisyon: {tlKomisyon15} TL")
        son_fiyat.config(text=f"Son Fiyat: {tlDegeriSon} TL")
    except ValueError:
        #TL_Yazisi.config(text="xkedyyy \n error")
        madduck.place(x=182,y=75)
        


always_on_top = tk.BooleanVar()

def update_always_on_top():
    # Set the "always on top" attribute based on the state of the checkbox
    root.attributes("-topmost", always_on_top.get())


# This is the section of code which creates a button
Button(root, text='Hesapla', bg='#696969', font=('arial', 12, 'normal'), command=change_text).place(x=26, y=55)

always_on_top_checkbox = tk.Checkbutton(root, text="Ustte Kal", font=('arial', 9, 'normal'), bg='#696969', variable=always_on_top, command=update_always_on_top)
always_on_top_checkbox.place(x=26,y=100)


temizle = Button(root, text='sil', bg='#696969', font=('arial', 9, 'normal'), command=clrText)
temizle.place(x=120,y=100)

root.mainloop()

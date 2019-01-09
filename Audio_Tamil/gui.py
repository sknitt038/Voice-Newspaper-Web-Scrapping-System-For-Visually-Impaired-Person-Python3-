from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import os
import newspapermodule
#return_values={}
def combob():
    inputValue = box_value.get()
    newspapermodule.mainmodule(inputValue)
def aboutus():
    messagebox.showinfo("About Us", "This software is developed by SURESH KUMAR from NIT TRICHY MCA Computer Science Department under the guidance of Dr.S.SANGEETHA Assistant Professor Of Computer Computer Applications Department.\nPurpose of the development of this sofware is to extract the genuine text content by removing unwanted content like adds and other mislanious items.\n After this text content is converted into audio. \n\nSo, basically this project is for VISUALLY IMPAIRED PERSON")
def hp():
    messagebox.showinfo("Help", "1. Select the Voice-Newspaper Website url\n2. Coinfrm that you have selected correct url\n3. After that press button named VIEW RESULT\n4. Then your default system browser is trigger and result are displayed\n5. And the result is converted into speach.\n6. Thanks")
def browser():
   messagebox.showinfo("Supported Browser List", "1. Internet Explorer \n2. Google Chrome \n3. Mozila Firefox \n4. Safari")
def contact():
   messagebox.showinfo("Contact Us", "      Suresh Kumar\nMobile:- 9470779814\nEmail-Id:- sureshkaum07896@gmail.com")
def onclick2():
    inputValue2=textbox.get("1.0","end-1c")
    newspapermodule.mainmodule(inputValue2)

root = Tk()
root.state('normal')
root.title("Voice-Newspaper Web Scrapping System")
root.configure(background = '#e1d8b9')

#----------------------------------Frame Section------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#----------------------------------TopFrameStart--------------------------------------------------------------------------------
topframe = Frame(root, highlightbackground="black", highlightthickness=5, width=1900, height=100)
topframe.configure(background = '#e1d8b9')
topframe.pack(side=TOP)

thelabel6 = Label(topframe, compound=TOP)
thelabel6.configure(background = '#e1d8b9')
thelabel6.pack(anchor=N)

img = ImageTk.PhotoImage(Image.open("/home/suresh/Desktop/Web-Scrapping-of-voice-newspaper-for-the-visually-Impaired--master/Audio_Tamil/download.jpg"))
panel = Label(topframe, image = img, compound=LEFT)
panel.configure(background = '#e1d8b9')
panel.pack(side = "left", fill = "both", expand = "1")

titlelabel = Label(topframe, text="WELCOME TO THE VOICE NEWSPAPER WEB SCRAPPING SYSTEM", font=('Noto Sans CJK TC Black', 21, 'bold','underline'), fg="saddle brown",compound=TOP)
titlelabel.configure(background = '#e1d8b9')
titlelabel.pack(anchor=N)
titlelabel1 = Label(topframe, text="Life is really simple, but we insist on making it complicated", font=('Noto Sans CJK TC Black', 19, 'bold','underline'), fg="saddle brown",compound=TOP)
titlelabel1.configure(background = '#e1d8b9')
titlelabel1.pack(anchor=N)
titlelabel2 = Label(topframe, text="*Source**Service**Solution*", font=('Noto Sans CJK TC Black', 17, 'bold','underline'), fg="saddle brown",compound=TOP)
titlelabel2.configure(background = '#e1d8b9')
titlelabel2.pack(anchor=N)
thelabel1 = Label(topframe, compound=TOP)
thelabel1.configure(background = '#e1d8b9')
thelabel1.pack(anchor=N)
#--------------------------------------------------------------------------------------------------------------------------------------------------

thelabel20 = Label(root)
thelabel20.pack()
thelabel21 = Label(root)
thelabel21.pack()

#-------------------------------------- Top1FrameStart----------------------------------------------------------------------------------------
topframe1 = Frame(root, highlightbackground="black", highlightthickness=5, width=900, height=50)
topframe1.configure(background = '#e1d8b9')
topframe1.pack(side=TOP)

thelabel11 = Label(topframe1, text="____________________________________________________________________________________________________________________",compound=TOP)
thelabel11.configure(background = '#e1d8b9')
thelabel11.pack(anchor=N)
thelabel10 = Label(topframe1, text="Enter The Any Specific Url For Which You Want to check", font=('Cooper Black', 15,'underline'), fg="midnight blue", compound=TOP)
thelabel10.configure(background = '#e1d8b9')
thelabel10.pack(side=TOP)
thelabel4 = Label(topframe1)
thelabel4.pack()
textbox = Text(topframe1, height=2, width=110)
textbox.pack(side=TOP)
thelabel12 = Label(topframe1)
thelabel12.pack()
buttonfortxtbox = Button(topframe1, text="Check Result", font=('Cooper Black', 9), fg="red", bg="white", bd=10, width=20,command=onclick2)
buttonfortxtbox.pack(anchor = S)
#-------------------------------------------------------------------------------------------------------------------------------------------

thelabel22 = Label(root)
thelabel22.pack()
thelabel23 = Label(root)
thelabel23.pack()

#-----------------------------------------Top2FrameStart-------------------------------------------------------------------------------------
topframe2 = Frame(root, highlightbackground="darkgreen", highlightthickness=5, width=700, height=500)
topframe2.configure(background = '#e1d8b9')
topframe2.pack(side=TOP)

thelabel2 = Label(topframe2, text="_______________________________________________________________________________________________________",compound=TOP)
thelabel2.configure(background = '#e1d8b9')
thelabel2.pack(anchor=N)
thelabel3 = Label(topframe2, text="Please Select The Desired Option From Given Link", font=('Cooper Black', 15,'underline'), fg="midnight blue",compound=TOP)
thelabel3.configure(background = '#e1d8b9')
thelabel3.pack(anchor=N)
thelabel25 = Label(topframe2)
thelabel25.pack()
thelabel9 = Label(topframe2, compound=TOP)
thelabel9.configure(background = '#e1d8b9')
thelabel9.pack(anchor=N)

box_value=StringVar()
combo = ttk.Combobox(topframe2, textvariable=box_value,state='readonly', width=50)
combo['values'] = ("http://www.bbc.com/news/world-asia-42126985", "https://www.gadgetsnow.com/tech-news/happy-to-receive-apple-awaiting-formal-proposal-says-prabhu/articleshow/61814415.cms?utm_source=toiweb&utm_medium=referral&utm_campaign=toiweb_hptopnews","http://money.cnn.com/2018/11/24/media/uma-thurman-harvey-weinstein-metoo/")
combo.current(0)
combo.pack()
thelabel24 = Label(topframe2)
thelabel24.pack()
buttonforcombo = Button(topframe2,text="Check Result", font=('Cooper Black', 9), fg="red", bg="white", bd=10, command=combob, width=20).pack()
thelabel13 = Label(topframe2)
thelabel13.pack(anchor=E)
thelabel14 = Label(topframe2)
thelabel14.pack(anchor=E)
#------------------------------------------------------------------------------------------------------------------------------------------------------

thelabel20 = Label(root)
thelabel20.pack()

#---------------------------------------------------BottomFrameStart-----------------------------------------------------------------------------------
bottomframe = Frame(root, width=800, height=300)
bottomframe.configure(background = '#e1d8b9')
bottomframe.pack(side=BOTTOM)

thelabel5 = Label(bottomframe, anchor=S)
thelabel5.configure(background = '#e1d8b9')
thelabel5.pack(anchor=N)
thelabel7 = Label(bottomframe, text="@Copyright By Suresh", font=(12),anchor=S)
thelabel7.configure(background = '#e1d8b9')
thelabel7.pack(anchor=N)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#------------------------DropDownMenu--------------------------
menu=Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Exit....")
submenu = Menu(menu)
menu.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="Help....", command=hp)
submenu.add_separator()
submenu = Menu(menu)
menu.add_cascade(label="About", menu=submenu)
submenu.add_command(label="Supported Browser", command=browser)
submenu.add_command(label="About Us", command=aboutus)
menu.add_cascade(label="Contact Us", menu=submenu)
submenu.add_command(label="Contact Us", command=contact)
submenu.add_separator()
submenu = Menu(menu)

thelabel8 = Label(root, anchor=S)
thelabel8.configure(background = '#e1d8b9', font=2)
thelabel8.pack(anchor=N)
root.mainloop()

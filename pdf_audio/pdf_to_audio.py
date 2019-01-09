#dependencies
# for python 3
from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import os
import PyPDF2
import pyttsx3

# for python 2 uncomment the following and comment the above one
# from Tkinter import *
# import tkFileDialog    #change tkFileDialog in line 17
# import PyPDF2
# import pyttsx3


def extract_text():
  '''To extract text from chosen PDF file'''
  file = filedialog.askopenfile(parent=root, mode='rb', title='Choose a PDF file')
  if file != None:
    pdfReader = PyPDF2.PdfFileReader(file)
    global mytext
    mytext = ""
    for pageNum in range(pdfReader.numPages):
      pageObj = pdfReader.getPage(pageNum)
      mytext += pageObj.extractText()
    file.close()


def stop_speaking(): 
  '''To stop the TTS engine on Stop click button'''
  engine.stop()


def speak_text():
       
    try:
        tts = gTTS(mytext, lang='en', slow=False)
        tts.save("out.mp3")
        os.system("mpg321 out.mp3")
    except:
        engine.say(mytext)
        engine.runAndWait()

def Application(root):
  '''Whole gui app'''
  root.geometry('{}x{}'.format(600, 500))       #for fixed size window
  root.resizable(width=False, height=False)
  root.title("PDF Orateur")
  root.configure(background="#e0ffff")

  frame1 = Frame(root, width=500, height=200, bg="#8a2be2")  #frame 1 for project name and desc.
  frame2 = Frame(root, width=500, height=450, bg="#e0ffff")   #frame 2 for rest part
  frame1.pack(side="top", fill="both")
  frame2.pack(side="top", fill="y")

  #frame 1 widgets
  name1 = Label(frame1, text="PDF Orateur", fg="white", bg="#8a2be2", font="Arial 28 bold")
  name1.pack()
  name2 = Label(frame1, text="A simple PDF Audio Reader for you!", fg="white",
                bg="#8a2be2", font="Calibri 15")
  name2.pack()

  #frame 2 widgets
  btn = Button(frame2, text='Select PDF file', command=extract_text, activeforeground="red", 
                padx="70", pady="10", fg="white", bg="black", font="Arial 12")
  btn.grid(row=0, pady=20, columnspan=2)

 
  # rate.focus_set()

  

  submitBtn = Button(frame2, text='Play PDF file', command=speak_text, activeforeground="red",
               padx="60", pady="10", fg="white", bg="black", font="Arial 12")
  submitBtn.grid(row=4,column=0, pady=65)

  #stop button
  stopBtn = Button(frame2, text='Stop playing', command=stop_speaking,activeforeground="red",
             padx="60", pady="10", fg="white", bg="black", font="Arial 12")
  stopBtn.grid(row=4, column=1, pady=65)





if __name__ == "__main__":
    #global vars
    
    engine = pyttsx3.init()
    
    root = Tk()
    Application(root)
    root.mainloop()


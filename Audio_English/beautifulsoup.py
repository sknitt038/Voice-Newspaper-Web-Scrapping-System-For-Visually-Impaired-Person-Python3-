from gtts import gTTS
import os

'''
from urllib.request import urlopen
import nltk

from bs4 import BeautifulSoup
import webbrowser

url = input("Enter the news website url:- ")
html = urlopen(url).read()
soup = BeautifulSoup(html)
[s.extract() for s in soup('script')]
x = soup.get_text()
y = "".join(x.split("\n"))
y = "".join(y.split("\r"))
y = "".join(y.split("-"))
y = "".join(y.split("."))
y = "".join(y.split(">"))
y = "".join(y.split("|"))
y = "".join(y.split("'"))
y = "".join(y.split("^"))
print(y)'''
'''

file = open("/home/abhishek/Desktop/Completed Module/save.html", "w")
file.write(str(y))
file.close()
webbrowser.open('/home/abhishek/Desktop/Completed Module/save.html')'''
myobj = gTTS(text="hello sir,i am suresh kamar", lang='en', slow=False)
myobj.save("sample1.mp3")
os.system("mpg321 sample1.mp3")

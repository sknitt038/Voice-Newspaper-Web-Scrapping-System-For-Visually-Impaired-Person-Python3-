from newspaper import Article
from gtts import gTTS
import os
import webbrowser

def mainmodule1(url):
    article = Article(url, language="hi")
    article.download()
    article.parse()
    return article.title

def mainmodule2(url):
    article = Article(url, language="hi")
    article.download()
    article.parse()
    return article.authors
def mainmodule3(url):
    article = Article(url, language="hi")
    article.download()
    article.parse()
    return article.text
def mainmodule(url):
    #url1 = "http://edition.cnn.com/2017/11/13/europe/theresa-may-russia/index.html"
    url1=url
    print(url1)
    title = "News Title:- "
    result1 = title + str(mainmodule1(url1))
    author = "Author Name:- "
    result2 = author + str(mainmodule2(url1))
    result3 = str(mainmodule3(url1))
    result = result1 +"\n"+"\n"+ result2 +"\n"+"\n"+ result3

    file = open("/home/suresh/Desktop/Web-Scrapping-of-voice-newspaper-for-the-visually-Impaired--master/Audio_Tamil/output.html", "w")
    file.write("<h1>")
    file.write("<center>")
    file.write(result1)
    file.write("</center>")
    file.write("</h1>")
    file.write("<h3>")
    file.write("<center>")
    file.write(result2)
    file.write("</center>")
    file.write("</h3>")
    file.write("<body bgcolor=rgb(7,0,0)>")
    file.write("<p>")
    file.write(result3)
    file.write("</p>")
    file.write("</body>")
    file.close()

    webbrowser.open('/home/suresh/Desktop/Web-Scrapping-of-voice-newspaper-for-the-visually-Impaired--master/Audio_Tamil/output.html')

    mytext = result
    language = 'ta'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")

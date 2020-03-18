import requests
from bs4 import BeautifulSoup
#-------website : http://coreyms.com-------
#with open("portfolio-website/assignment-12/assignment12.html") as file:
#soup =BeautifulSoup(file,"lxml")
#------implementing the soup for extracting the defined class and paragraph----
'''match = soup.title.text
match = soup.div
match=soup.find("div",class_="medium")
match = soup.find("div",class_="intro")
headline =match.p.text
print(headline)
print(soup.prettify())'''
#-------using find_all method-------
#k=soup.find_all("a",class_="links")
#print(k)
'''for i in soup.find_all("li",class_="link-container"):
    print(i.text)'''
#------------getting url from corey website and parsing the utube link into required way and merging them by using split ----------
'''source = requests.get("http://coreyms.com").text

print(type(source))
soup = BeautifulSoup(source,"html.parser")
article = soup.find("article")
print(article.prettify())
vid_src = article.find("iframe",class_="youtube-player")["src"]
print(type(vid_src))
vid_id =vid_src.split("/")
print(vid_id)
vid_id = vid_src.split("/")[4]
print(vid_id,type(vid_id))
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)'''
#-----------extracting a particular class- div  & paragraph elements
'''anchor = article.h2.a.text
print(article.prettify())
summary = article.find("div",class_="entry-content").p.text
print(summary)'''

#---------inspect a website------
'''source = "https://imdb.com"
right click on it and  "INSPECT"
 for other operations refer beautifulsoup by corey 
'''
#-----try and except bloock-----
'''try:
    source = requests.get("http://coreyms.com").text
#print(type(source))
    soup = BeautifulSoup(source,"html.parser")
    article = soup.find("article")
#print(article.prettify())
    vid_src = article.find("iframe",class_="youtube-player")["src"]
#print(type(vid_src))
    vid_id =vid_src.split("/")
    print(vid_id)
    vid_id = vid_src.split("/")[4]
#print(vid_id,type(vid_id))
    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)
except Exception as e:
    yt_link = none

print(yt_link)'''

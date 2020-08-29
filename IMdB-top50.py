import pandas as pd
import numpy as np
from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup

inp_year=input("Enter the year")
custom_url="https://www.imdb.com/search/title/?title_type=feature&release_date="+str(inp_year)+"-01-01,"+str(inp_year)+"-12-31&countries=us"

names=[] 
runtime=[]
genre=[]
director=[]
cast=[]
rating=[]
metascore=[]
desc=[]

page=urlopen(custom_url)
html=(page.read()).decode("utf-8")
soup=BeautifulSoup(html,"html.parser")

tags=soup.find_all('div', attrs = {'class' : 'lister-item-content'})

for lines in tags:
    
    title_cols=lines.find_all("h3",class_="lister-item-header")
    p_tag=lines.find_all("p",class_="text-muted")
    p_crew=lines.find_all("p",class_="")
    rate=lines.find_all("div",class_="ratings-bar")
    
    decr=p_tag[1]
    desc.append(decr.text.strip())
    
    for t in title_cols:
        names.append(t.a.text)
    for t in p_tag:
        r=t.find_all("span",class_='runtime')
        g=t.find_all("span",class_='genre')
        for i in r:
            runtime.append(i.text)
        for i in g:
            genre.append(i.text.strip())
    for t in rate:
        m=t.find_all("div",class_="inline-block ratings-metascore")
        rating.append(t.strong.text)
        if m==[]:
            metascore.append(0)
        else:
            for i in m:
                metascore.append(i.span.text.strip())
    for line in p_crew:
        a_tags=line.find_all("a")
        crew=[]
        for a in a_tags:
            crew.append(a.text)
        director.append(crew[0])
        cast.append(crew[1:])
     
csv_file = open('imdb-top50.csv','w',encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name','Runtime','Genre',"Description",'Director','Cast','IMdB Rating','Metascore'])
 
for i in range(len(names)):
    csv_writer.writerow([names[i],runtime[i],genre[i],desc[i],director[i],cast[i],rating[i],metascore[i]])
 
csv_file.close()

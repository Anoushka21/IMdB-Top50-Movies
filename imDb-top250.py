import numpy as np
import pandas as pd
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
#This is basic scrapper scrapping top 250 movies
url="https://www.imdb.com/chart/top"
page=urlopen(url)
html=(page.read()).decode("utf-8")
soup=BeautifulSoup(html,"html.parser")
movies=soup.tbody
movies=movies.find_all("tr")
names=[]
ratings=[]
directors=[]
cast=[]
year=[]
for td in movies:
    title_col=td.find_all("td",class_="titleColumn")
    rating_col=td.find_all('td',class_="ratingColumn imdbRating")
    for i in title_col:
        names.append(i.a.text)
        year.append(i.span.text)
        t=i.a['title'].split("(dir.), ")
        directors.append(t[0])
        cast.append(t[1])
    for i in rating_col:
        ratings.append(i.strong.text)
csv_file = open('imdb-top250.csv','w',encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name','Year of Release','Director','Cast','User Rating'])
 
for i in range(len(ratings)):
    #print(names[i], "Year" ,year[i],"Director",directors[i],"Cast",cast[i], "| Rating:",ratings[i])
    csv_writer.writerow([names[i],year[i],directors[i],cast[i],ratings[i]])
 
csv_file.close()

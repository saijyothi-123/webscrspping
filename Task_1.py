import requests
import json
from bs4 import BeautifulSoup
import pprint
url="https://www.imdb.com/india/top-rated-indian-movies/"
page=requests.get(url)
# print(page)

soup = BeautifulSoup(page.text,"lxml")
# print(soup.prettify())

list_data = []

table_data=soup.find("table",attrs={"class":"chart full-width"})   
# print(table_data)

table_rows=table_data.find_all("tr")
# print(table_rows)

for data in table_rows[1:]:
    
    position = data.find("td",{"class":"titleColumn"}).text.strip()
    rank = ''
    for i in position:
        if '.'not in i:
            rank = rank + i
        else:
            break
    # movie_rank.append(rank)
    # print(movie_rank)
    
    title = data.find("td",{"class" : "titleColumn"})
    # print(title.a.text)
    
    rating = data.find("td",{"class":"ratingColumn imdbRating"})
    ratingData = rating.strong.text
    print(ratingData)
    
    year_of_release = data.find("td",{"class":"titleColumn"})
    yearData = year_of_release.span.text.replace("(",'').replace(")",'')
    # print(yearData)
    
    link = data.find("td",{"class" : "titleColumn"})
    movie_link = link.a['href']
    movie_url = "https://www.imdb.com" + movie_link
    # print(movie_url)
    
    list_data.append({
        'position':int(rank),
        'title':title.a.text,
        'rating':float(ratingData),
        'year_of_release':int(yearData),
        'movie_url':movie_url,
        
    })
print(list_data)
pprint.pprint(list_data)


open_file=open("imdb_data","w")
json.dump(list_data,open_file,indent=4)
open_file.close


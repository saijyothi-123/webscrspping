import json
import os
import pprint
with open("imdb_data_1","r") as f:
        data = json.load(f)
        # print(data)
def group_by_year(movies):
    years = []
    for i in data:
        # print(i)
        year = i["year_of_release"]
        # print(year)
        if year not in years:
                years.append(year)
        # print(years)
    movie_dict={i:[]for i in years}   
    for i in data:
            year = i['year_of_release']   
        #     print(year) 
            for x in movie_dict:
                    if str(x) == str(year):
                            movie_dict[x].append(i)
    return(movie_dict)    
                            

print(group_by_year(data))
pprint.pprint(group_by_year(data))

open_file=open("imdb_data_2","w")
json.dump(group_by_year(data),open_file,indent=4)
open_file.close

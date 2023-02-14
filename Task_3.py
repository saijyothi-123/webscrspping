import json
import os
import pprint
with open("imdb_data_2","r") as f:
        data = json.load(f)
        # print(data)
def group_by_decade(movie):
    moviedec = {}
    list1 = []
    for index in data:
        # print(index)                 year
        mod = int(index) % 10
        # print(mod)                   mod = 3
        decade = int(index )- mod
        # print(decade)                decade=1970
        if decade not in list1:
            list1.append(decade)      
    # print(list1)                     creating list of decades
    list1.sort()
    # print(list1)
    for i in list1:
        moviedec[i] = []
    for i in moviedec:
        dec10 = i+9
        # print(dec10)                 dec10 = 1959
        for x in data:
            # print(x)
            if int(x) <= dec10 and int(x) >= i:
                for v in data[x]:
                    moviedec[i].append(v)
        
    return(moviedec)
print(group_by_decade(data))
pprint.pprint(group_by_decade(data))

open_file=open("imdb_data_3","w")
json.dump(group_by_decade(data),open_file,indent=4)
open_file.close

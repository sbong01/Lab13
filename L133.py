#Rosemary, Krista, and Saerin
import dbm
db1=dbm.open("base","c")
db1["dinner.jpeg"]="a plate of tacos"
db1["flower.jpeg"]="carnation"
db1["animal.jpeg"]="turtle"
db1["sport.jpeg"]="soccer"
db1["drink.jpeg"]="coffee"

db1["sport.jpeg"]="football"
db1["drink.jpeg"]="soda"

for item in db1:
    print(item,db1[item])



db1.close()

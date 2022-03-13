car = {
"make": "ford",
"model" :"focus",
"year" :"2006",
"owner" :{
    "name":"Ruth",
    "driver-number":234}

}

attr ="year"



#print(car["year"])
#print (type(car["owner"].get("names")))

for key in car:
    print (key, "has value", car[key])

for key, value in car.items():
    print(key + "has a value",value)
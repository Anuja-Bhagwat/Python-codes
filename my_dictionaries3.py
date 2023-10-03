country_captials ={
        "India":"New Delhi",
        "Japan":"Tokyo",
        "Sri Lanka":"Colombo",
        "Germany":"Berlin"
}
for x in country_captials:  # Print all key names in dictionary one by one
    print(x)

for x in country_captials.keys(): #Second method
    print(x)
  

for x in country_captials: # Print all value names in dictionary one by one
    print(country_captials[x])

for x in country_captials.values(): #Second method
    print(x)

for x, y in country_captials.items(): #Loop through both key and values by using item() method
    print("Key:",x,"Value:",y)

#Copy Dictionaries

new_country_captials = country_captials.copy() #Make a copy of a dictionary with the copy() method
print(new_country_captials)

new_country_captials = dict(country_captials)  #Make a copy of a dictionary with the dict() built in function
print(new_country_captials)

#Nested Dictionaries
#Create a dictionary containing three dictionaries
myfamily = {
  "child1" : {
    "name" : "Emily",
    "year" : 2004
  },
  "child2" : {
    "name" : "Sofia",
    "year" : 2007
  },
  "child3" : {
    "name" : "Marcin",
    "year" : 2011
  }
}
print(myfamily) # Print dictionary
print(myfamily["child2"]["name"]) #Access the item from nested dictionaries
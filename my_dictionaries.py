#Create dictionary containing the details of mobile phone
my_phone={
    "brand":"Samsung",
    "model":"A14",
    "launch date":"January 2023",
    "color":"Light Green"
}
print(my_phone)  #Print entire dictonary enteries
print(my_phone["brand"]) #Print a specific item from dictionary
print(len(my_phone)) #Print the length of dictionary using len() function
print(type(my_phone)) #Find the data type of dictionary

#Accessing the items from dictionaries.
x = my_phone["model"]  #Access the item by using the ["key name"] 
print(x)

y = my_phone.get("launch date") #Access the item using get() method
print(y)

x = my_phone.keys()  #The keys() method will return a list of all the keys in the dictionary.
print(x)

x = my_phone["price"] ="Rs 23000/-" #Add a new item to dictionary and print it.
print(my_phone)

x = my_phone.values() #The values() method will return a list of all the values in the dictionary.
print(x)


x = my_phone["color"] ="White" #Make a change in the item and print the dictionary
print(x)

if "brand" in my_phone:
    print("Yes!! brand is present in phone dictionary")

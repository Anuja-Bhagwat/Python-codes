mysets = {"Red","Blue","Yellow"}  #Created a set
print(mysets)

mysets = {"Red",'Blue','Yellow','Green','Red'}  #Duplicate items are not allowed. Set items can get printed at any order.
print(mysets)

mysets = {"Red","Blue","Yellow",1, False,0} # In Sets ["True" or 1 ] and ["False" or 0] are consider as same values
print(mysets)

country = {"India","Germany","Italy","America","Japan"} # len() function used to find no. of items in set
print(len(country))

print(type(country))  # Identify the data type of set using type() function

colors = set(('Red','Blue','Yellow','Orange','Green')) #Using set() constructor to make a set
print(colors)

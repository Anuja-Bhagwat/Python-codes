# Convert tuple into list, and add item, return again to tuple

fruits  = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
x = list(fruits) # Convert tuple to list
print(x) # Print converted list.
x.append("coconut") # Add new item to list
print(x) #Print updated list
fruits = tuple(x) #Convert updated list back to tuple
print(fruits) #Print updated tuple

#Concatenate tuples
tuple1 = ("Apple","Mangoes","Banana")
tuple2 = ("Red","Yellow","Blue")
tuple3 = tuple1 + tuple2
print(tuple3)

#Tuple count() method
t1 =(1,3,5,6,3,7,8,3,6,2,3,6,2)
x = t1.count(3)
print("The no. of time 3 appears in tuple is",x)

#Tuple index() method
tuple = (1,4,5,7,3,6,7,3,7,1,5,7,9)
y = tuple.index(7)
print("The 7 element appear at index",y)
z = tuple.index(3, 5, 9)
print("The no. 3 appear at index",z,"between index position 5 to index position 9")
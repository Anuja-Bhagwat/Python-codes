tuples1 = ("Red","Yellow","Black","Orange","Pink","Blue")
print(tuples1)
print(len(tuples1))  # Find the length of tuple using len() function

#Create tuple with only one item followed by ,
tuples2 = ("Apple",)  # This is example of tuple
print(type(tuples2))
tuples2 = ("Apple")   #This is not a tuple. This is a simple string example
print(type(tuples2))

#Check if item is present in tuple
c= (input("Enter the country name:"))
country = ("India","Germany","Italy","SriLanka")
if (c in country):
    print("India is present in the given tuple")
else:
    print("This country is not present in tuple")

#Access the elements from tuple
print(country[2])   # Print the item at index 2
print(country[-3])  # Negative Indexing

#Print items in specific range of indexes
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[3:6]) 


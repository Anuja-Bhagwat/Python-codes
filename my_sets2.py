# Access the items from sets
fruits = {"Apple","Banana","Mango","Cherry"}
for x in fruits:
 print(x)

# Check if item is present in sets
my_fruit = (input("Enter the fruit name:-"))  # Take input from user & check item is present/not in set
if (my_fruit in fruits):
 print(my_fruit,"is present in given set")
else:
 print("Fruit is not present in set")

if 'Apple' in fruits:   # Define a item to check
 print('Apple is in set')

#Add items to sets
fruits.add('Orange')
print("New Updated Set is",fruits)

#Update items from one set to other set
even_no = {2,4,6,8,10}
odd_no = {1,3,5,7,9}
even_no.update(odd_no)
print(even_no)

#Remove items from sets using remove() method
fruits.remove("Cherry")
print(fruits)

#Remove items from sets using discard() method
sets1 = {"Python","Java","Javascript","C Programming"}
sets1.discard("Java")
print(sets1)

#Remove any random item from sets
remove_item = sets1.pop()
print(remove_item)
print(sets1)

#clear() method empties the entire set
fruits.clear()
print(fruits)

#copy() method creates a copy of set
planets = {'Earth','Jupiter','Mars','Venus'}
planets.copy()
print(planets)


#Python codes to demostrate list

#append() method add an element at end of the list. 
num=[]  #Creating an empty list
num.append(12)   #Appending data in list
num.append(6.7)
num.append("String")
print(num) # Print the list

#clear() method removes all elements from list.(Empty list)
fruits=['apples','banana','cherries','mangoes']
print(fruits)  # This will print entire list
fruits.clear()
print(fruits)  #This will print empty list

#copy() method will return a copy of list.(Duplicate list)
list1=['apples','banana','cherries','mangoes']
list2=list1.copy()
print(list2)

# count() method will return the count or number of times the element is present in list
list1=['apples','banana','cherries','mangoes','berries','apples']
x=list1.count('apples')  #This will return the count of elements in list
print("The count of apples in list is ",x)

# extend() method will add all the elements of one list into other at the end of the list
odd_list=[2,4,6,8]   #First List
even_list=[1,3,5,7,9] #Second List
even_list.extend(odd_list) 
odd_list.extend(even_list)
print("Complete List after extend",even_list)
print("Complete List after extend:- ",odd_list)

#insert() method will add a element at a specific given postion
vowels=['a','e','i','u'] #Create a list of vowels
print("List before insert() method:- ",vowels)
vowels.insert(3,'o') # Insert the element 'o' at index 3 (4th position)
print("List after insert() method:- ",vowels)

#remove() method will remove a element which is passed as argument from list
prime_numbers=[2,3,5,7,9,11]
print(prime_numbers)
prime_numbers.remove(9)
print("Updated List :- ",prime_numbers)

#pop() method will remove a element from specific position.
language=['English','Marathi','Tamil','German','Hindi']
removed_element=language.pop(3)
print("Removed Element:- ",removed_element)
print("Updated List:- ",language)

#reverse() method will reverse all the elements from list
language.reverse()
print("Updated List :- ",language)

#sort() method will sort all the elements in ascending order.
list3=[10,50,60, 40,20, 80,100]
list3.sort()
print("Updated List:- ",list3)
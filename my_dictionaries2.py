student = {
       "name" : "Divya",
       "Roll_no" : "BEIT136",
       "Score" : "First Class",
       "Passing Year" : 2018
    }

student["Passing Year"] = 2019 #change the value of a specific item by referring to its key name
print(student)

student.update({"Passing Year" : 2020}) #The update() method will update the dictionary with the items from the given argument.
print(student)

student["branch"] = "Computer" #Adding an item to the dictionary 
print(student)

student.pop("Passing Year") #To remove item from dictionary use pop() method
print(student)

student.popitem() # popitem() method removes the last inserted item in dictionary
print(student)

del student["Score"] #The del keyword removes the item with the specified "[key name"]
print(student)

student.clear() # clear() method is used to empty the dictionary
print(student)
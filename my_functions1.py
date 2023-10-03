#Function Arguments
# Python code to demonstrate the use of default arguments   
def fun(n1,n2=20):
    print("Number 1 is",n1)
    print("Number 2 is",n2)
fun(50)   #Calling the function and assigning only one arguement
fun(50,30) #Passing two arugments to the function

# Python code to demonstrate the use of keyword arguments 
def fun(n1,n2):   
    print("Number 1 is",n1)
    print("Number 2 is",n2)
fun(40,60)  # Calling function and passing arguments without using keyword   

fun(n1=40,n2=60)  # Calling function and passing arguments using keyword   

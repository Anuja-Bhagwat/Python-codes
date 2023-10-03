#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_fun(*kids):
    print("The youngest child is",kids[2])

my_fun("Emily","Olivia","James")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Passing a list as an argument
def funct(fruits):
   for x in fruits:
      print(x)
fruits = ["Apple","Cherry","Mango"]
funct(fruits)

#Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass statement.   # The function definition cannot be empty.
def my_funct():
   pass

 #Else and finally block
def divide (x,y):
    try:
      result = x/y
      print(int(result))
    except ZeroDivisionError:
       print("Denominator cannot be zero")
    else:
       print("The result is:-",result)
    finally:
       print("This block is always executed")

divide(3,0)
divide(50,10)

# Raise Exception
level = -1
if level <0:
   raise Exception("Level Cannot be less than zero")

x = "hello"
if not type(x) is int:
   raise TypeError ("Only integers are allowed")
   



    
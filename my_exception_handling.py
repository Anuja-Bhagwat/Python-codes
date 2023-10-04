# Try and exception block 
a = input("Enter the number:")
print(f"Multiplication table of {a} is")
try:
    for i in range(1,11):
     print(f"{int(a)} X {i}  = {int(a) *i}")
except :
   print("Invalid!! Input should be number only")

print("End of program")

# Many Exceptions
try:
    a = [6,3]
    num = (int(input("Enter a integer:")))
    print(a[num])
except ValueError:
   print("Number entered is not integer")
except IndexError:
   print("Index is out of range")
   
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
print(a)
print(b)
print(c)
if (a>b) and (a>c):
    print(a,"is the largest number")

if(b>a) and (b>c):
    print(b,"is the largest number")

else:
    print(c,"is the largest number")
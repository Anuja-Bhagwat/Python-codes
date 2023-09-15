# range() function always start from 0  and increment by 1 (default)
for x in range(10):
    print(x)

print("\n")

# range() function will always start from 1st element in given range but will not incude the last element 
for x in range(2,9):
    print(x)
print("\n")    

#range() function 1st position is starting value, 2nd position is end value in sequence, 3rd position is the increment value
for x in range(1,20,3): # Will print the sequence from 1 with increment of 3 upto 20 
    print(x)
#String Indexing 
str = "Welcome to Atos"
print(str[4])   #Fetch the character from left 
print(str[-3])  #Fetch the character from right

#String Slicing in Python
print(str[0:7])  #Start from index 0 upto [index]-1
print(str[0:  :2]) 
print(str[ :6]) #Slice from start upto index 6
print(str[3:]) #Slice to the end

#Modify Strings
a = "   Hello World!  "
print(a.upper())  #Modify the string to upper case
print(a.lower())  #Modify te string to lower case
print(a.strip())  #strip() method will remove the whitespaces in string
print(a.replace("Hello","Namaste"))  #replace() method will replace a character or a word in string

sentence = "I am Mark"
print(sentence.split()) #spilt() method will split the string into substring
print(len(sentence))  #len() check the length of string

txt = "The best things in life are free"
print("best" in txt)  # Check if any phrase or character is present in string use keyword 'in'
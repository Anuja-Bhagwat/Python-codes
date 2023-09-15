marks=int(input("Enter the marks:"))
print("Your marks is",marks)

if (marks>85) and (marks<100):
    print("Your score is A grade")

elif(marks>=60) and (marks<=85):
    print("Your score is B grade")

elif(marks>=35) and (marks<60):
    print("Your score is C grade")

else:
    print("You are fail")

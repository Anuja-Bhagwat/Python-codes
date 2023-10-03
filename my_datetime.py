import datetime     #Import date and time module
x = datetime.datetime.now()  #Display current date and time
print(x)
print(x.year) # Display current  year

date1 = datetime.date(1998,4,5)  #create a specific date object
print(date1)

from datetime import date
date1 = date(2023,6,20)
print("Date1=",date1)
print("Year = ",date1.year)
print("Month = ",date1.month)
print("Day = ",date1.day)

#Getting Minimum date
min_date = date.min
print("Minimum Date:-",min_date)

#Getting maximum date
max_date = date.max
print("Maximum Date:-",max_date)
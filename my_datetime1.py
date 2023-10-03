import datetime
date1 = datetime.datetime(2023,1,1)
x = datetime.datetime.now()
print(x)

print("Short Version of Day:-",date1.strftime("%a"))  # %a is short version of Weekday
print("Full Version of Day:-",date1.strftime("%A"))  # %A is full version of Weekday

print("Short Version of Month:-",date1.strftime("%b"))  # %b is short version of Month
print("Full Version of Month:-",date1.strftime("%B"))   # %B is short version of Month

print("Short Version of Year:-",date1.strftime("%y"))  # %y is short version of Month
print("Full Version of Year:-",date1.strftime("%Y"))   # %Y is short version of Month

print("WeekDay as number:-",date1.strftime("%w"))  # %w is weekday as number.(0 = Sun,1 = Mon...)
print("Week number of year:-",date1.strftime("%W"))   # %B is short version of Month

print("24 Hours Format:-",x.strftime("%H"))  # %H is Hours in 24 hours format(0-23)
print("12 Hours Format:-",x.strftime("%I"))  # %I is Hours in 12 hours format(0-12)

print("Current Time in AM/PM:-",x.strftime("%p"))  # %p is current time in am/pm

print("Current Minutes:-",x.strftime("%M"))  # %M is current minutes
print("Current Seconds:-",x.strftime("%S"))  # %S is current seconds
print("Current Microseconds:-",x.strftime("%f"))  # %M is current microseconds

print("Day number of Year:-",x.strftime("%j"))  # %j is day number of year out of 365 day

print("Local Version of date:-",x.strftime("%x"))  # %x is local version of date
print("Local Version of time:-",x.strftime("%X"))  # %X is local version of time
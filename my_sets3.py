# union() method returns a new set with combination of both set.
#union() & update() methods are same
set1 = {'a','b','c'}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

#The intersection_update() method will keep only the items that are present in both sets.
x = {"Google","Apple","Microsoft"}
y = {"Amazon","Facebook","Google"}
x.intersection_update(y)
print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
z = x.intersection(y)
print(z)

x.symmetric_difference_update(y)
print(x)

z = x.symmetric_difference(y)
print(z)

x.difference_update(y)
print(x)

z = x.difference(y)
print(z)
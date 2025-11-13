t=(1,4,3,8,5)
print(t)
print(type(t))
# tuple are immutable
# unlike list we cannot change the value of tuple
print(t.count(3))
# count is used to count the number of times a value occurs in the tuple
print(t.index(5))
# index is used to find the  first index of a value in the tuple
print(len(t))
print(1 in t)
# in is used to check whether a value is present in the tuple or not
a={
    "bhumika":20,
    "kavya":19,
    "zennerah":18,
    19:0,
    "list":[2,5,6],
}
print(a["zennerah"])
print(a[19])
print(a["list"])
print(a.items())
# items is used to print all the key value pairs of the dictionary
# into a list of key value pairs in the form of tuples
print(a.keys())
print(a.values())
a.update({"sakshi":21})
print(a)
#  dictionary are mutable
# we can easily access the value by using the key of the dictionary 
# while in list we have to use the index to access the value
# as compared to list dictionary are faster and more efficient and also more flexible than list 
print(a.get("bhumika"))
# a(["bhumika"]) this will give an error if the key is not present in the dictionary
# but using get method it will return none if the key is not present in the dictionary
print(a.get("hetal")) # this will return none as hetal key is not present in the dictionary
# print(a["hetal"]) # this will give an error as hetal key is not present in the dictionary
print(a.pop("kavya")) # pop method removes the key value pair from the dictionary
print(a.popitem())
# popitem method removes the last key value pair from the dictionary
print(a)
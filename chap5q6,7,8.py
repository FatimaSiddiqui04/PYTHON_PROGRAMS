d={}
name=input("enter your name1:")
lang=input("input language1:")
d.update({name:lang})
name=input("enter your name2:")
lang=input("input language2:")
d.update({name:lang})
name=input("enter your name3:")
lang=input("input language3:")
d.update({name:lang})
name=input("enter your name4:")
lang=input("input language4:")
d.update({name:lang})
print(d)
print(type(d))
# if two names are same then the last entered language will be considered for that name
# if two languages are same for different names then both names will be stored with same language value

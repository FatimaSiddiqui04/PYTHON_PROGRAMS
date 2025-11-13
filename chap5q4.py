s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len((s)))
#  float 20.0 is considered equal to integer 20 in a set, so only two unique elements are stored.
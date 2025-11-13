a=int(input("enter any number :"))
b=int(input("enter any number :"))
c=int(input("enter any number :"))
d=int(input("enter any number :"))

if(a>b and a>c and a>d):
    print(a)

elif(b>a and b>c and b>d):
    print(b)

elif(c>a and c>b and c>d):
    print(c)

elif(d>a and d>b and d>c):
    print(d)

else:
    print("none") 

print("end of the program")

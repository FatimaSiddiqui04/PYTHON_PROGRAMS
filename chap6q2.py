a=int(input("enter subject marks:"))
b=int(input("enter subject marks:"))
c=int(input("enter subject marks:"))

total_percentage=(((a+b+c)/300)*100)
a_percentage=(((a)/100)*100)
b_percentage=(((b)/100)*100)
c_percentage=(((c)/100)*100)


if (total_percentage>=40 and a_percentage>=33 and b_percentage>=33 and c_percentage>=33):
    print("pass")

elif(total_percentage<0 and a_percentage<0 and b_percentage<0 and c_percentage<0):
    print("value cant be negative")

else:
    print("fail")

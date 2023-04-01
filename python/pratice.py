a1=int(input("Enter the first number"))
a2=int(input("Enter the second number"))
a3=int(input("Enter the third number"))
a4=int(input("Enter the fourth number"))

if(a1>a4):
    f1=a1
else:
    f1=a4
if(a2>a3):
    f2=a2
else:
    f2=a3
if(f1>f2):
    print(str(f1)+"greater number")
else:
     print(str(f2)+"greater number")
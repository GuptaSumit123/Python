m1=int(input("Enter the marks of the first subject  "))
m2=int(input("Enter the marks of the second subject  "))
m3=int(input("Enter the marks of the third subject  "))

if(m1<33 or m2<33 or m3<33):
    print("your are fall in the exam")
elif(m1+m2+m3)/3 < 40:
    print("your are fail in the exam beause ur not gor above 40%")
else:
    print("Congratulation  your pass the exam")

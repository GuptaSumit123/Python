def greater(num1,num2,num3):
    if(num1>num3 and num1>num2):
        
            return num1        
    if(num2>num3 and num2>num1):
        return num2 
    else:
        return num3
a=int(input("Enter the 1st number "))
b=int(input("Enter the 2nd number "))
c=int(input("Enter the 3rd number "))

res=greater(a,b,c)
print("Greater number is " + str(res))


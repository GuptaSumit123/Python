num=int(input("Enter a number :"))
for i in range(2,num):
    if (num%i == 0):
        print(num,"not prime")
        break
    else:
        print(num," prime number")

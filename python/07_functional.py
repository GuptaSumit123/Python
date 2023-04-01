def rec_sum(n):
    if n<=1:
        return n
    else:
        return n + rec_sum(n-1)
n=int(input("Enter any postive  number "))

if n<0:
    print("Enter a postive number" )
else:
    print("the sum is",rec_sum(n))
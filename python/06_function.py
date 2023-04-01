def farenheit(c):
    return (c* (9/5)) +32

c=int(input("Enter the celsius value "))
f=farenheit(c)
print("farenheit is " + str(f))
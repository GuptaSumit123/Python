#wap to create a list of n elements and find the length  of the list using list() function
test_list = []
n=int(input("Enter the list size\n"))
for i in range(0,n):
    print("Enter number at index ",i)
    item=int(input())
    test_list.append(item)
    print("user list is :",test_list)

print("The list is : " + str(test_list))
counter = 0
for i in test_list:
    counter = counter + 1
print("Length of list  : " + str(counter))
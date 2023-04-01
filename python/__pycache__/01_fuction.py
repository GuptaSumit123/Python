def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1=[78,98,23,45]
percentage1=percent(marks1)

marks2=[43,56,76,44]
percentage2=percent(marks2)

print(percentage1,percentage2)


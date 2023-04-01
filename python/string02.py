letter='''Dear |<Name>|
          your are selected candidate for your dream job
          Today |<Date>|'''
name=input("Enter the candidate name\n")
date=input("Enter today date\n")
letter= letter.replace("|<Name>|",name)
letter=letter.replace("|<Date>|",date)
print(letter) 
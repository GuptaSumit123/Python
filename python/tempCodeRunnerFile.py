letter='''Your |<Name>|
          your are selected candidate 
          Today |<Date>|'''
Name=input("Enter the candidate name\n")
Date=input("Enter today date\n")
letter=letter.replace("|<Name>|", Name)
letter=letter.replace("|<Date.|", Date)
print(letter)
def remove_an_split(string,word):
    newstr=string.replace(word," ")
    return newstr.strip()
name="here is Sumit gupta"
n=remove_an_split(name,"Sumit")
print(n)
 
    
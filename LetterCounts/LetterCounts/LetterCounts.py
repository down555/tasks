print("Enter a word wth small latin letters:")
word=input()
ecount=word.count('e') 
acount=word.count('a') 
icount=word.count('i') 
ucount=word.count('u') 
ocount=word.count('o') 
vowels=ecount+acount+icount+ucount+ocount # total vowels calculation

print("Total vowels:",vowels) 

print("Total consonants:",len(word)-vowels)  # total consonants calculation

if (ecount==0):

    print ("There is no e in word, False")

else:

    print("Total e=",ecount)

if (ucount==0):

    print ("There is no u in word, False")

else:

    print("Total u=",ucount)

if (ocount==0):

    print ("There is no o in word, False")

else:

    print("Total o=",ocount)

if (acount==0):

    print ("There is no a in word, False")

else:

    print("Total a=",acount)

if (icount==0):

    print ("There is no i in word, False")

else:

    print("Total i=",icount)


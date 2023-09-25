string=(input())
cleanstring=' '.join(string.split())
if len(cleanstring)>1000:
    print("Too long") 
else:
    print(cleanstring)

"""Anagram or Not"""
def anagramOrNot(s1,s2):
    sl1=list(s1)
    sl2=list(s2)
    sl1=sorted(sl1)
    print(sl1)
    sl2=sorted(sl2)
    print(sl2)
    if(len(sl1)!=len(sl2)):
        return False
    else:
        for i in range(0,len(sl1)):
            if(sl1[i]==sl2[i]):
                i=i+1
            else:
                return False
        return True



s1=str(input("Enter s1"))
s2=str(input("Enter s2"))
f=anagramOrNot(s1,s2)
if(f==True):
    print("Yes")
else:
    print("No")

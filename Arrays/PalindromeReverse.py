"""Reverse a String"""
def ReverseString(t):
    s=list(t)
    p=s.copy()
    startPt=0
    endPt=len(s)-1
    while(startPt<=endPt):
        s[startPt],s[endPt]=s[endPt],s[startPt]
        startPt=startPt+1
        endPt=endPt-1
        if(p==s):
            return True
        else:
            return False
if __name__=="__main__":
    s="Madam"
    f=ReverseString(s.lower())
    if(f==True):
        print("It is a Plaindrome")
    else:
        print("It is Not")



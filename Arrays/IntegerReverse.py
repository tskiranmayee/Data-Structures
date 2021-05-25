""" Reverse the number and check same or not"""


def reverseInteger(n):
    p=n
    s=0
    while(n>0):
        r = n % 10
        s=s*10+r
        n = n // 10

    if(p==s):
        return True
    else:
        return False


n=int(input())
f=reverseInteger(n)
if(f==True):
    print("Yes")
else:
    print("No")
"""Palindrome or not"""
def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False


if __name__=="__main__":
    s="Madam"
    f=palindrome(s.lower())
    if(f==True):
        print("Yes")
    else:
        print("No")

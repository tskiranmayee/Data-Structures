"""Reverse a List or an Array"""

def reverseList(n):
    startPt=0
    endPt=len(n)-1
    while(startPt<=endPt):
        n[startPt],n[endPt]=n[endPt],n[startPt]
        startPt=startPt+1
        endPt=endPt-1
    return n

if __name__=="__main__":
    n=[1,2,3,4,5]
    n=reverseList(n)
    print(n)

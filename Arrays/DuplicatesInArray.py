"""Find Duplicates in array"""
def duplicateOrNot(arr):
    for i in arr:
        if(arr[abs(i)]>=0):
            arr[abs(i)]=-arr[abs(i)]
        else:
            return True



arr=[1,2,0,3]
f=duplicateOrNot(arr)
if(f==True):
    print("Duplicate found")
else:
    print("Duplicate not found")
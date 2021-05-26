"""Find Duplicates in array"""
def duplicateOrNot(arr):
    for i in arr:
        if(arr[abs(i)]>=0):
            arr[abs(i)]=-arr[abs(i)]

        else:
            print("Duplicate found for {}".format(abs(i)))
            return True


arr=[1,2,2,3]
f=duplicateOrNot(arr)
if(f==True):
    pass
else:
    print("Duplicate not found")
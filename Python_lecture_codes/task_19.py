arr = [1,2,3,4,6]
target = int(input("enter your target"))
if(target not in arr):
    for i in range(len(arr)):
        if(arr[i]>target):
            print("target will be added at index",i)
for i in range(len(arr)):
    if(arr[i]==target):
        print("target found at index ",i)
    
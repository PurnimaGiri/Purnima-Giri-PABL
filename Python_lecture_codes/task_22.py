arr = [56,67,30,79]
arr.sort()
if(len(arr)%2==0):
    mid_1=arr[(len(arr)//2)]
    mid_2=arr[((len(arr)//2))-1]
    print((mid_1+mid_2)/2)
else:
    print("The median is ",arr[int(len(arr)/2)])
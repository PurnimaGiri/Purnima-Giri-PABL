arr = [1,2,3,4,5]
sum = 5
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if(arr[i]+arr[j]==sum):
           if(i == j):
               continue
           else:
               print(i,j)
   
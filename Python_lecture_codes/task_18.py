arr = [2,3,-8,7,-1,2,3]
current_sum = 0
maximum_sum = arr[0]
for i in arr:
    current_sum = current_sum +i
    maximum_sum = max(maximum_sum,current_sum)
    if(current_sum<0):
        current_sum = 0
print(maximum_sum)

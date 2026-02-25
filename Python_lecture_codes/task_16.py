# homework
arr = [1,5,3,6]
k = 3
arr.sort()
print(arr[k-1])

arr1 = [1,8,4,7]
union = list(set(arr) | set(arr1))
print(union)

print("maximum minimum without built in")
list = []
n = int(input("enter the number of values"))
for i in range(n):
    item = int(input("enter the number"))
    list.append(item)
print(list)
max = list[0]
min = list[0]
for i in list:
    if i > max:
        max = i
    
print("maximum",max)
print("minimum",min)


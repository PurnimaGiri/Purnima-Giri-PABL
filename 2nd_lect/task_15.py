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
    if i < min:
        min = i
print("maximum",max)
print("minimum",min)


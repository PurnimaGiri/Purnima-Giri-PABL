list = []
n = int(input("enter the number of values "))
for i in range(n):
    item = int(input("enter the number"))
    list.append(item)
print(list)
l=len(list)
rev = []
for i in range(l-1,-1,-1):
    rev.append(list[i])
print("The reversed array is ",rev)
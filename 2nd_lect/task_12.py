list = []
n = int(input("enter the number of values"))
for i in range(n):
    item = int(input("enter the number"))
    list.append(item)
print(list)
print("reverse of array")
list.reverse()
print(list)
list = []
n = int(input("enter the number of values"))
for i in range(n):
    item = int(input("enter the number"))
    list.append(item)
print(list)


sum = 0
for i in range(0,len(list)):
    sum = sum + list[i]
print("The sum of elements in list is ",sum)



print("accessing elements")
for i in list:
    print(i)
n1 = int(input("enter the index you want to change"))
v1 = int(input("enter the value"))
list[n1] = v1
print("updated list is ",list)
print("adding element")
list.append(v1)
print("updated list is ",list)
print("deleting element")
list.remove(v1)
print("updated list is ",list)
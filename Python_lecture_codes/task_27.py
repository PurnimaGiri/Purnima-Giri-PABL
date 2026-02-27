arr = ['abc','abc','y','z','y']

dict = {}
for i in arr:
    dict[i] = arr.count(i)
print(dict)
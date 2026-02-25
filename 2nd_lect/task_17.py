# arr = [1,2,3,4,36]
# temp = []
# last = arr.pop()
# temp.append(last)
# for i in range(len(arr)):
#     temp.append(arr[i])
# print(temp)
def clockwise(arr):
    last = arr.pop()
    arr.insert(0,last)
    return arr
print(clockwise([1,2,3,4,5]))
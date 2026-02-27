arr = ["x","y","x"]
#Array contains the votes maximum votes is the candidate winner
dict = {}
for i in arr:
    dict[i] = arr.count(i)
print("winner is ",max(dict,key = dict.get))
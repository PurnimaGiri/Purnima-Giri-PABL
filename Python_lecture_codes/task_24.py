s = ["tax","bat","tab","tea","eat"]
grp = {}
for i in s :
    sw = "".join(sorted(i))
    if sw in grp :
        grp[sw].append(i)
    else:
        grp[sw] = [i]
print(list(grp.values()))

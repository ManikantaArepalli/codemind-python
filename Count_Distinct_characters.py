ns=input()
s=ns.lower()
a=[]
for i in s:
    if i not in a and i not in " ":
        a.append(i)
print(len(sorted(a)))
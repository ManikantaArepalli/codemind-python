s=input().split()
a=[]
for i in s:
    a.append(min(i))
    a.append(max(i))
print(*a)
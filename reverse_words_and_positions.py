s=input().split()[::-1]
a=[]
for i in s:
    a.append(i[::-1])
print(*a)
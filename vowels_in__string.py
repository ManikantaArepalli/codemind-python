s=input()
a=[]
f=0
for i in s:
    if i in 'aeiouAEIOU':
        if i not in a:
            a.append(i)
            f=1
if f:
    print(*a)
else:
    print(-1)
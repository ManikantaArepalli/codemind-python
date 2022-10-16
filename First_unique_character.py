s=input().lower().replace(' ','')
a=[]
c=0
for i in s:
    if i not in a:
        a.append(i)
for i in a:
    if s.count(i)==1:
        print(i)
        break
else:
    print(-1)
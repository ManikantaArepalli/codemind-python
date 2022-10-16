s=input().lower().replace(' ','')
a=[]
for i in s:
    if i not in a:
        a.append(i)
ns=sorted(a)
for i in ns:
    if s.count(i)==1:
        print(i,end='')
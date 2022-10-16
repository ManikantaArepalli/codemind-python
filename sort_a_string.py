s=input()
n=[]
a=[]
for i in s:
    if i.isalpha():
        n.append(i)
    else:
        a.append(i)
n.sort()
k=0
c=0
for i in s:
    if i.isalpha():
        print(n[k],end='')
        k+=1
    else:
        print(a[c],end='')
        c+=1
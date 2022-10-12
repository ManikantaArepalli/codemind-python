n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
c=0
for i in l:
    if i not in b:
        b.append(i)
for i in b:
    a.append(l.count(i))
for i in range(len(a)):
    if a[i]==b[i]:
        c+=1
print(c)
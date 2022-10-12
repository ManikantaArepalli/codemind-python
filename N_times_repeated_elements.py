n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
flag=0
for i in set(l):
    c=l.count(i)
    if c==k:
        a.append(i)
        flag=1
if flag==1:
    print(*a)
else:
    print(-1)
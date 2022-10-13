n=int(input())
l=list(map(int,input().split()))
a=[]
if n%2==0:
    print(*l)
else:
    for i in l:
        a.append(i)
    a.append(0)
    print(*a)
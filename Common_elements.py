n,m=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
a=[]
for i in l:
    if i not in a:
        a.append(i)
for i in a:
    if i in p:
        print(i,end=' ')
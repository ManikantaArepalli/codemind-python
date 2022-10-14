n,m=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
a=[]
for i in l:
    if i not in p:
        print(i,end=' ')
for i in p:
    if i not in l:
        print(i,end=' ')
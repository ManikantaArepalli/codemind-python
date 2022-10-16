n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i>=0:
        a.append(len(str(i)))
    else:
        i=-1
        a.append(len(str(i)))
print(a.count(k))
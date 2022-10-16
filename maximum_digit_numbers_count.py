n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i>=0:
        a.append(len(str(i)))
    else:
        i=-i
        a.append(len(str(i)))
k=max(a)
for i in range(n):
    if a[i]==k:
        print(l[i],end=' ')
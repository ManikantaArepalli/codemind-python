n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i not in a:
        c=l.count(i)
        a.append(i)
        print(i,c,end=' ')
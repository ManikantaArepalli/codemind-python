n=int(input())
l=list(map(int,input().split()))
nl=[]
for i in l:
    s=0
    while(i!=0):
        r=i%10
        s=s*10+r
        i//=10
    nl.append(s)
print(*nl)
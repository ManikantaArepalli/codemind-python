a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=0
for i in set(l1):
    if i in set(l2):
        c+=1
print(c)
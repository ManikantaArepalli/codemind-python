n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(set(a))
d=list(set(b))
count=0
for i in c:
    if i not in d:
        count+=1
for i in d:
    if i not in c:
        count+=1
print(count)
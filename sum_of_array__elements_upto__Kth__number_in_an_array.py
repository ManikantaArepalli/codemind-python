n=int(input())
l=list(map(int,input().split()))
Sum=0
k=int(input())
s=l.index(k)
for i in range(s+1):
    Sum+=l[i]
print(Sum)
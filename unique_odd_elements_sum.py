n=int(input())
l=list(map(int,input().split()))
Sum=0
k=list(set(l))
for i in k:
    if i%2!=0:
        Sum+=i
print(Sum)
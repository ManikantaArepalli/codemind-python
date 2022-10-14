n=int(input())
l=list(map(int,input().split()))
Sum=0
for i in l:
    if i%2!=0:
        break
    else:
        Sum+=i
print(Sum)
n=int(input())
l=list(map(int,input().split()))
Sum=0
a=[sum(map(int,list(str(i)))) for i in l]
for i in a:
    Sum+=i
print(Sum)
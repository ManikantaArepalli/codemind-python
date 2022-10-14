n=int(input())
l=list(map(int,input().split()))
s,e=map(int,input().split())
Sum=0
a=[]
for x in range(s,e+1):
    a.append(x)
for i in l:
    if i in a:
        Sum+=i
print(Sum)
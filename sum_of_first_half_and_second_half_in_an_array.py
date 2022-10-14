n=int(input())
l=list(map(int,input().split()))
Sum,Sum1=0,0
for i in l:
    if l.index(i)<=l.index(n//2):
        Sum+=i
    else:
        Sum1+=i
print(Sum)
print(Sum1)
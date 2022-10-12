n=int(input())
k=list(map(int,input().split()))
res=sum(list(set(k)))
print(res)
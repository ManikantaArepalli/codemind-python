def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
c=0
Sum=0
l=list(map(int,input().split()))
for i in l:
    if i>1:
        if isprime(i):
            Sum+=i
            c+=1
avg=Sum/c
print("%.2f" %avg)
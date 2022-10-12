def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
flag=0
for i in range(int(n**0.5)+1):
    if is_prime(i):
        for j in range(int(n**0.5)+1,n):
            if is_prime(j):
                if i*j==n:
                    print(i,j)
                    flag=1
if flag==0:
    print(-1)
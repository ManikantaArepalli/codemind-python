def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return "not a prime";
    else:
        return "prime";
n=int(input())
print(is_prime(n))
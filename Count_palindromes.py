def is_palin(n):
    s=str(n)
    if s[::-1]==s:
        return 1
    else:
        return 0
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if is_palin(i):
        c+=1
print(c)
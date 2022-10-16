s=input().split()
a=[]
for i in s:
    r=abs(ord(max(i))-ord(min(i)))
    a.append(r)
print(*a)
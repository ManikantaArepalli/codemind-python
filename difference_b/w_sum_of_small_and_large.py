s=input().split()
a=[]
b=[]
for i in s:
    a.append(ord(min(i)))
    b.append(ord(max(i)))
print(sum(b)-sum(a))
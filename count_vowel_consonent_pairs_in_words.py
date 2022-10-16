s=input().split()
c=0
for i in s:
    x=0
    y=-1
    for j in range(len(i)):
        if i[x] in "aeiouAEIOU" and i[y] not in "AEIOUaeiou":
            c+=1
        x+=1
        y-=1
print(c)
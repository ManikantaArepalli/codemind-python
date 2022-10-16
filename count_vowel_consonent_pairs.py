s=input()
l=len(s)
c=0
x=0
y=-1
for i in range((l//2)):
    if s[x] in "aeiouAEIOU" and s[y] not in " AEIOUaeiou":
        c+=1
    elif s[x] not in " aeiouAEIOU" and s[y] in "AEIOUaeiou":
        c+=1
    x+=1
    y-=1
print(c)
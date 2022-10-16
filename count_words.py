s=input().lower().split()
c=0
for i in s:
    if i[0] in 'aeiou' and i[-1] not in 'aeiou':
        c+=1
print(c)
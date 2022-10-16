s=input().lower().replace(' ','')
c=0
for i in s:
    if i.isalpha():
        continue
    else:
        c+=1
print(c)
s=input().lower().split()
for i in s:
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    print(c,end=' ')
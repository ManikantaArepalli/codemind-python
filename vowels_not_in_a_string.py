a=input().replace(' ','')
s='aeiou'
d=[]
flag=1
for i in a:
    if i in s and i not in d:
        d.append(i)
d.sort()
d=''.join(d)
for i in s:
    if i not in d:
        print(i,end=' ')
        flag=0
if flag:
    print(0)
n=input()
l=[]
for i in n:
    l.append(i)
s=len(l)
ss=set(l)
sss=len(ss)
if s==sss:
    print("Unique Number")
else:
    print("Not Unique Number")
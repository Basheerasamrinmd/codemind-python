l,r,x=list(map(int,input().split(" ")))
count=0
for i in range(l,r+1):
    if i%x==0:
        count+=1
print(count)
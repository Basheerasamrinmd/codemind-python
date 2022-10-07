a,b=list(map(int,input().split()))
if a>b:
    n=a
else:
    n=b
    
while 1:
    if(n%a==0 and n%b==0):
        print(n)
        break
    else:
        n=n+1
    
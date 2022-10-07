n=int(input())
a=1
b=0
print(b,end=' ')
print(a,end=' ')
for i in range(0,n-2):
    c=a+b
    b=a
    a=c
    print(c,end=' ')
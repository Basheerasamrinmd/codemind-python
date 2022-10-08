n=int(input())
a=n*n
sum=0
while a>0:
    rem=a%10
    sum=sum+rem
    a=a//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")
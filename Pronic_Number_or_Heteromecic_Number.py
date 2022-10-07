import math
flag=0
i=0
n=int(input())
while i <= (int(math.sqrt(n))):
    if n == i * (i + 1):
        flag = 1
        break
    i = i + 1

if flag == 1:
    print("YES")
else:
    print("NO")


import math
p,r,t=list(map(int,input().split(" ")))
a=p*(pow((1+r/100),t))
print("{:.2f}".format(a))
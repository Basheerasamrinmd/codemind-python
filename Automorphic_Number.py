n=int(input())
nod=len(str(n))
sq=n*n
lastdi=sq%pow(10,nod)
if n==lastdi:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
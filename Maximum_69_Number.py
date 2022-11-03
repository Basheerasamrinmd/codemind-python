n=int(input())
r=list(map(int,str(n)))
if r[0]==6:
    r[0]=9
    print(int("".join(map(str,r))))
elif r[1]==6:
    r[1]=9
    print(int("".join(map(str,r))))
elif r[2]==6:
    r[2]=9
    print(int("".join(map(str,r))))
elif r[3]==6:
    r[3]=9
    print(int("".join(map(str,r))))
else:
    print(n)
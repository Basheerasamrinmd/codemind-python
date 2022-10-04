n=int(input())
a=str(n)
b=len(a)
if (b<10):
    print("Invalid")    
elif (a[1]==0):
    print("Invalid")
else:
    print("Valid")
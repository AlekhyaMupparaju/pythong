a=int(input("\nenter a value"))
b=list(str(a))
c=0
d=1
e=len(b)
while(e>0):
    d=d*int(b[c])
    c=c+1
    e=e-1
print("\n",d)

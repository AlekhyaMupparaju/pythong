a=int(input("Enter a number "))
d=[]
e=0
while(a>0):
    print(a)
    d.insert(e,a)
    e=e+1
    a=a/2
print(list(reversed(d)))

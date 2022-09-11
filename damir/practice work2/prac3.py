from cmath import sqrt
print("ax2 + bx +c = 0")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=(b**2)-(4*a*c)
e=(((b-2*b)+sqrt(d))/2*a)
f=(((b-2*b)-sqrt(d))/2*a)
g=(b-2*b)/2*a
if d<0:
    print("error")
elif d==0:
    print(g)
elif d>0:
    print("x1=",e)
    print("x2=",f)
    


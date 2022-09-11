from cmath import pi, sqrt
a=str(input("# = rectangle, ^ =  triangle , @ = circle :"))
if a=="#":
    x=int(input("first length:"))
    y=int(input("secong lengh:"))
    recarea=x*y
    print("area is :",recarea)

elif a=="^":
    x1=int(input("first length:"))
    y1=int(input("secong lengh:"))
    z1=int(input("third lengh:"))
    p=(x1+y1+z1)/2
    triarea=sqrt(p*(p-x1)*(p-y1)*(p-z1))
    print("area is :",triarea)
elif a=="@":
    r=int(input("radius:"))
    circarea=pi*pow(r,2)
    print("area is :",circarea)
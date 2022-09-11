from cmath import sqrt
import math
from tokenize import Double
x=int(input("number 1:"))
y=int(input("number 2:"))
h=sqrt(math.cos(2*y)+math.sin(4*y)+(sqrt(math.exp(x)+math.exp(x-(2*x))))) / pow((math.exp(x-(2*x)+math.exp(x))),3)*pow((math.sin(4*y)+math.cos(2*y)-2),2)
print("The answer:",h)
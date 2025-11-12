import math
a=int(input("Ingrese un número"))
b=0
c=0
d=a
e=0
while a>=1:
    a/=10
    b+=1
print("El número de cifras es",b)
while d>0:
    e=d%10
    c+=e
    d=math.trunc(d/10)
print("La sumatoria es", c)

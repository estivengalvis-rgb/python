import math
a=float(input("Ingrese un número "))
cnt=0
sum=0
b=a
c=a
d=0
e=0
while a>=1:
    a=a/10
    cnt+=1
while b>0:
    d=b%10
    b=math.trunc(b/10)
    e=d**cnt
    sum+=e
if sum==c:
    print("Sí es un número de Armstrong")
else:
    print("No es un número de Armstrong")


a=float(input("Ingrese los primeros intervalos "))
b=float(input("Ingrese los primeros intervalos "))
c=float(input("Ingrese los siguientes intervalos "))
d=float(input("Ingrese los siguientes intervalos "))
e=float(input("Ingrese los últimos intervalos "))
f=float(input("Ingrese los últimos intervalos "))
g=float(input("Ingrese un número"))
if g>a and g<b or g>c and g<d or g>e and g<f:
    print("Su número está dentro de los intervalos")
else:
    print("Su número no está dentro de los intervalos")
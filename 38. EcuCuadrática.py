print("Ingrese los datos de la ecuación cuadrática")
a=float(input("Ingrese a "))
b=float(input("Ingrese b "))
c=float(input("Ingrese c "))
d=b**2-(4*a*c)
if d>=0:
    print("La ecuación cuadrática si tiene solución")
else:
    print("La ecuación cuadrática no tiene solución")
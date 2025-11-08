a=int(input("Ingrese el dinero que quiere invertir"))
b=int(input("Ingrese el porcentaje de interes"))
c=int(input("Ingrese los días"))
d=b/100
e=(a*d*c)/360
print("Los valores de los interes son ", e)
f=e*0.07
print("El descuento del 7% es ", f)
g=a+e-f
print("La cantidad de dinero que tiene ahora es", g)
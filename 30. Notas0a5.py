a=float(input("Ingrese su calificación "))
if a>=5:
    print("Excelente")
elif a<5 and a>=4:
    print("Sobresaliente")
elif a<4 and a>=3.5:
    print("Aceptable")
elif a<3.5 and a>=3:
    print("Pasó")
else:
    print("Insuficiente")
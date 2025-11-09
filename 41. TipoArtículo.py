print("Textil/Electrodoméstico/ElementoCocina/VideoJuego")
a=str(input("Ingrese el tipo de artículo "))
if a=='Textil' or a=='textil':
    print("No tiene descuento")
elif a=='Electrodoméstico' or a=='electrodoméstico':
    print("Tiene un descuento del 3.7%")
elif a=='ElementoCocina' or a=='Elementococina' or a=='elementococina':
    print("Tiene un descuento del 4.2%")
elif a=='VideoJuego' or a=='Videojuego' or a=='videojuego':
    print("Tiene un descuento del 7.8%")
else:
    print("Opción Invalida")
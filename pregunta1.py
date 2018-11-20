#Construya una aplicación que solicite 1 coordenada “x” y “y” y determine la distancia que hay
#entre el punto indicado y el punto 0, 0.
#Imprima la distancia y la coordenada ingresada al terminar la app.
import math
x = float(input("Ingrese el número de la coordenada x:"))
y = float(input("Ingrese el número de la coordenada y:"))

distancia = math.sqrt(x**2+ y**2)

print("La coordenada ingresada en el eje x es:", x)
print("La coordenada ingresada en el eje y es:", y)
print("La distacia entre la coordenada ingresada:(",x,",",y,") y el punto(0,0) es:", distancia)
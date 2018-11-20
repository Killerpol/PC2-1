#Construya una aplicación que solicite 5 números al usuario y desarrolle una función llamada
#“menor_en_arreglo” que solicite un arreglo de números y calcule el valor menor de sus elementos
#(sin usar la función min).

a = []
i=0
while len(a)<5:
    i=i+1
    n = int(input(u"Ingrese número:"))
    a.append(n)

menorN = a[0]

def menor_en_arreglo (a):
    for i in a:
        if i < menorN:
            menorN = i
        

print(menorN)
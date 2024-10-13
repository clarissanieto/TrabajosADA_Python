# 2. Ejercicio de while y for
# Desarrolla un programa que haga lo siguiente:
# 1. Usar un bucle while para pedir al usuario que ingrese números hasta que se ingrese el número 0.

numeros = []
while True:
    entrada_numeros = int(input("Introduce una serie de numeros, favor de ingresar un 0 para detener la entrada de numeros: "))
    if entrada_numeros == 0:
        break 
    numeros.append(entrada_numeros)
    print(numeros)

# 2. Usar un bucle for para calcular la suma de los números ingresados, excluyendo el 0.

suma = 0
for numero in numeros:
    suma += numero
print("La suma de los numeros ingresadoa es de: ", suma)



    
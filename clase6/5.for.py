# Programa para imprimir cuadrados de numeros y calcular la suma

# Lista de numeros
numeros = [1,2,3,4,5]

# Inicializacion de la variable
suma_cuadrados = 0

# Iterar sobre cada numero en la lista
for numero in numeros: 
    # Calcular el cuadrado del numero
    cuadrado = numero **2
    # Imprimer el cuadrado
    print(f"El cuadrado de {numero} es {cuadrado}")
    #Agregar cuadrado a la suma
    suma_cuadrados += cuadrado 
    
# Imprimir 
print(f"La suma de los cuadrados es {suma_cuadrados}")

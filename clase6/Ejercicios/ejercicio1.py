# 1. Ejercicio de Sets y for
# Crea un programa que reciba una lista de números y realice las siguientes operaciones:
# 1. Crear un set a partir de la lista para eliminar duplicados.

numeros = [1,2,2,3,4,5,5,6,7,7]
conjunto = set(numeros)
print("Conjunto: ", conjunto)

# 2. Iterar sobre el set e imprimir cada número.
for numero in conjunto:
    print(numero)
    
# 3. Contar cuántos números son mayores que un valor dado y almacenarlos en un nuevo set.
valor_dado = 3
numeros_mayores_a_3 = set()

for numero in conjunto:
    if numero > valor_dado:
        numeros_mayores_a_3.add(numero)
        print("Los numeros mayores a 3 dentro del set son: ", numeros_mayores_a_3)
    

        
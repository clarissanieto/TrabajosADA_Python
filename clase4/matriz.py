# Definir una matriz de 3x3
matriz = [
    [1, 2, 3], # Fila 0
    [4, 5, 6], # Fila 1
    [7, 8, 9]  # Fila 2
]

# Acceder y mostrar algunos elementos especificos de la matriz
print("Algunos elementos de la matriz: ")
print("Elementos en la fila 0, columna 0: ", matriz[0][0])
print("Elemento en la fila 1, columna 2: ", matriz[1][2])

# Modificar elementos especificos de la matriz

print("\nModificando elementos especificos: ")
matriz[0][1] = 10 # Cambair el elemento en la fila 0, columna 1 a valor 10
matriz [2][0] = 15 
print("Matriz después de las modificaciones: ")
print(matriz)

# Acceder a una fila completa
print("\nAccediendo a una fila completa: ")
fila_completa = matriz[1] # Obtener toda la fila
print("Fila completa en la posicion 1: ", fila_completa)

# Reemplazar una fila complera
print("\nReemplazando una fila completa: ")
matriz[1] = [20, 21, 22]
print("Matriz después de reemplazar la fila 1: ")
print(matriz)

# Trabajar con una submatriz (parte de una matriz)
submatriz = [matriz[0][1:3], matriz[1][1:3]] # Extraer submatriz de las columnas 1 a 2 de las filas 0 y 1
print("Submatrix extraida: ", submatriz)

# Mostramos toda la matriz al final
print("\nMatriz completa al final: ")
print(matriz[0])
print(matriz[1])
print(matriz[2])

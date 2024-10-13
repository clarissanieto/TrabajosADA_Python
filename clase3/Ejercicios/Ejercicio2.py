# Crea un programa que tome una lista de números y calcule la suma de una
# sublista especificada por el usuario.
# Instrucciones:
# • Define una lista de números predefinida.
# • Pide al usuario que ingrese el índice de inicio y el índice de fin para la sublista.
# • Usa slicing para obtener la sublista.
# • Suma los elementos de la sublista.
# • Muestra la suma.

mi_lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # Definir lista
print("Lista de números: ", mi_lista) # Imprimir lista

# Pedir al usuario el inicio y final de la sublista
inicio_sublista = int(input("Ingrese el índice del inicio de la sublista: ")) # Agregar int (si no, sale error)
final_sublista = int(input("Ingrese el índice de fin de la sublista: "))

# Obtener sublista por slicing
sublista = mi_lista[inicio_sublista:final_sublista]

# Sumar los elementos de la sublista
suma_sublista = sum(sublista)
print("La suma de la sublista es: ", suma_sublista) # Imprimir suma de la sublista


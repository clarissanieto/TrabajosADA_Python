# Ejercicio 1: Contador de Números Específicos: Escribe un programa que cuente cuántas veces aparece un número 
# específico en una lista.
# Instrucciones:
# • Define una lista de números predefinida o pídele al usuario que ingrese los números.
# • Pide al usuario que ingrese un número a buscar.
# • Usa el método count() para determinar cuántas veces aparece el número en la lista.
# • Muestra el resultado.

mi_lista = [1,1,5,9,1,3,4,7,7] # Definir lista
print("Lista de números: ", mi_lista) # Imprimir lista

numero_a_buscar = input("Ingrese numero a buscar: ") # Pedir al usuario un número a buscar

repeticion_numero = mi_lista.count(1) # Cuantas veces aparece el número en la lista

# Imprimir el resultado de cuantas veces aparece el número en la lista
print(f"El número {numero_a_buscar} aparece {repeticion_numero} veces en la lista") 





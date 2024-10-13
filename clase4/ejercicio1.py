# Ejercicio 1: Operaciones Básicas con Tuplas
# • Crea una tupla llamada mi_tupla con los siguientes elementos: (5, 10, 15, 20, 25).
mi_tupla = (5, 10, 15, 20, 25)
print("Tupla: ", mi_tupla)

# • Usa el método count para contar cuántas veces aparece el número 10 en la tupla.
repeticion_10 = mi_tupla.count(10)

# • Usa el método index para encontrar la posición del número 20 en la tupla.
posicion_20 = mi_tupla.index(20)

# • Muestra los resultados de las operaciones anteriores.
print(f"El número 10 se repite {repeticion_10} vez (veces) en la tupla")
print(f"El número 20 se encuentra en la posición {posicion_20} en la tupla")



# Ejercicio 5: Manejo de Matrículas en una Tupla
# • Crea una tupla llamada matriculas con los siguientes números de matrícula: (101, 102, 103, 104, 105).
matriculas = (101, 102, 103, 104, 105)
print("Matrículas: ", matriculas)

# • Usa el método count para contar cuántas veces aparece el número de matrícula 102 en la tupla.
Repeticion_102 = matriculas.count(102)
print(f"El número de matrícula 102 se repite {Repeticion_102} vez en la tupla")

# • Usa el método index para encontrar la posición del número de matrícula 104 en la tupla.
posicion_104 = matriculas.index(104)
print(f"El número de la matrícula 104 se encuentra en la posición {posicion_104} de la tupla")


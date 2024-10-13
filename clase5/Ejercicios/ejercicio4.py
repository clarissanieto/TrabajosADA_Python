# Ejercicio 4: Lista de Diccionarios 
# 1. Crea una lista de diccionarios, donde cada diccionario representa un estudiante con las siguientes claves: 
#o Nombre 
#o Edad 
# o Calificaciones (que es una lista de números) 

estudiantes = [{"Nombre" : "Harry", "Edad":11, "Calificaciones" : [9,10,8,9,10]}, 
               {"Nombre":"Ron", "Edad":11, "Calificaciones": [7,8,9,10,8]},
               {"Nombre":"Hermione", "Edad":11, "Calificaciones": [10,10,10,10,10]}]
print("Estudiantes: ", estudiantes)

# 2. Imprime el nombre y las calificaciones del primer estudiante en la  lista. 

primer_estudiante =  estudiantes[0]
nombre = primer_estudiante["Nombre"]
calificaciones = primer_estudiante["Calificaciones"]

print("El nombre del primer estudiante es: ", nombre)
print("Las calificaciones del primer estudiante son: ", calificaciones)

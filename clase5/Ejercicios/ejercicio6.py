# Ejercicio 6: Anidación Compleja de Diccionarios y Listas 
# 1. Crea un diccionario que contenga información sobre una escuela. La escuela tiene: 
# o Nombre 
# o Año de fundación 
# o Lista de clases, donde cada clase es un diccionario con: 
# ▪ Nombre de la clase 
# ▪ Lista de estudiantes, donde cada estudiante es un diccionario con: 
# ▪ Nombre 
# ▪ Edad 

escuela = {
    "Nombre": "Hogwarts School of Witchcraft and Wizardy", 
    "Año de fundación": 992,
    "Clases": [
        {"Nombre": "Defensa contra las Artes Oscuras",
                "Lista de estudiantes": 
                    [{"Nombre": "Harry", "Edad": 15},
                     {"Nombre": "Hermione","Edad": 15},
                     {"Nombre":"Ron", "Edad": 15}]}, 
               {"Nombre": "Herbología",
                "Lista de estudiantes":
                    [{"Nombre": "Neville", "Edad": 15}, {"Nombre": "Hermione", "Edad": 15}]}
               ]
    }

print(escuela)

# 2. Imprime el nombre del primer estudiante de la primera clase. 
# Ir accediendo a cada uno de los dicccionarios y listas que lo componen
clases = escuela["Clases"] # Primero ingresar a las clases
primera_clase = clases[0] # Segundo: ingresar a la primera clase
lista_estudiantes = primera_clase["Lista de estudiantes"] # Tercero: Acceder a la lista de estudiantes de esa clase
primer_estudiante = lista_estudiantes[0] #Cuarto: Acceder a los datos del primer estudiante
primer_estudiante_nombre = primer_estudiante["Nombre"] # Quinto: Obtener el nombre del primer estudiante

print("El nombre del primer estudiante de la clase de Defensa contra las Artes Oscuras es: ", primer_estudiante_nombre)







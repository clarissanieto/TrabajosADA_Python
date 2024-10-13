# 1. Declaración de variables y constantes
edad = 25                 # Número
nombre = "Ana"            # Cadena de texto (string)
esta_estudiando = True    # Booleano

# Declaración de Constantes
PI = 3.14                 # Número
PAIS = "Argentina"        # Cadena de texto (string)

# 2. Leer Valores por teclado
edad = int(input("Introduce tu edad: "))         # Leer un número entero
nombre = input("Introduce tu nombre: ")          # Leer una cadena de texto
esta_estudiando = input("¿Estás estudiando? (si/no): ").lower() == "si"   # Leer y convertir a booleano

# 3. Tipos de datos
cantidad_de_libros = 10          # Número (int)
titulo_libro = "El Principito"   # Cadena de texto (string)
es_interesante = True            # Booleano (bool)
temas = ["Aventura","Fantasía","Filosofía"]   # Lista (Array)
autor = {                        #Diccionario (Objeto)
         "nombre": "Antoine de Saint-Exupéry",
         "nacionalidad": "Francesa"
         }

# Convertir Tipos de Datos
edad_str = str(edad)             # Convertir número a cadena de texto
cantidad_de_libros_float = float(cantidad_de_libros)  # Convertir entero a número de punto flotante

# 4. Imprimir Resultados en la consola
print("Nombre:", nombre)
print("Edad:", edad)
print("¿Está estudiando?", esta_estudiando)
print("Constante PI:", PI)
print("Constante País", PAIS)
print("Cantidad de libros:", cantidad_de_libros)
print("Título del libro:", titulo_libro)
print("¿Es interesante?", es_interesante)
print("Temas del libro:", temas)
print("Autor del libro:", autor)
print("Edad (como cadena de texto):", edad_str)
print("Cantidad de libros (como float):", cantidad_de_libros_float)


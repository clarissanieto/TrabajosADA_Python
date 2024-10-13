# Ejercicio 1: Crear y Acceder a un Diccionario Básico 
# 1. Crea un diccionario que contenga la siguiente información sobre un libro: 
# o Título, Autor, Año de publicación, Género 
libro = {
    "Título":"Fourth Wing",
    "Autor":"Rebecca Yarros",
    "Año de publicación":2023,
    "Género":"Fantasía-Romance"
}

print("Libro: ", libro)

# 2. Accede e imprime cada uno de estos valores usando las claves correspondientes. 
titulo = libro["Título"]
autor = libro["Autor"]
año_publicacion = libro["Año de publicación"]
genero = libro["Género"]

print("Título: ", titulo)
print("Autor: ", autor)
print("Año de publicación: ", año_publicacion)
print("Género: ", genero)

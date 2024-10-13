# Ejercicio 2: Modificar y Eliminar Elementos de un Diccionario 
# 1. Usando el diccionario del ejercicio anterior, actualiza el año de  publicación a 1968. 
libro = {
    "Título":"Fourth Wing",
    "Autor":"Rebecca Yarros",
    "Año de publicación":2023,
    "Género":"Fantasía-Romance"
}

print("Diccionario libro original: ", libro)

libro["Año de publicación"] = [1968]

print("Diccionario libro con año de publicación actualizado: ", libro)

# 2. Elimina el género del diccionario. 
del libro["Género"]

print("Diccionario libro con género eliminado: ", libro)

# 3. Imprime el diccionario después de cada operación.
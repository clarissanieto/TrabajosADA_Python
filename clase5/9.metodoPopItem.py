# Crear un diccionario
persona = {
    "nombre" : "Emilia",
    "edad" : 33,
    "profesion" : "Veterinaria"
}

# Imprimir el diccionario original
print("Diccionario original: ", persona)

# Usar popItem para eliminar y obtener el ultimo par clave-valor
ultimo_elemento = persona.popitem()

# Imprimir el par clave-valor
print("Ultimo par clave-valor eliminado: ", ultimo_elemento)

# Imprimir el diccionario después del popItem
print("Diccionario después de usar popItem: ", persona)


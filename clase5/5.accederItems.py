# Crear un diccionario
persona = {
    "nombre": "Alejandra",
    "edad": 30,
    "ciudad": "Merida"
}

# Usamos el metodo
pares_clave_valor = persona.items()

# Imprimir
print("Pares clve valor: ", pares_clave_valor)

# Pasarlo como lista
valores_lista = list(pares_clave_valor)
print(valores_lista)

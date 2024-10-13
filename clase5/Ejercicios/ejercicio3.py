# Ejercicio 3: Anidación Básica de Diccionarios 
# 1. Crea un diccionario que represente una persona con las siguientes claves: 
# o Nombre 
# o Edad 
# o Dirección (donde la dirección es otro diccionario con claves: Calle, Ciudad, Código postal)  
persona = {
    "nombre": "Clarissa",
    "edad": 24,
    "dirección": {
        "calle": "Reforma",
        "ciudad": "Ensenada",
        "codigo postal": "0000"
    } 
}

print("Diccionario Clarissa: ", persona)

# 2. Imprime la ciudad de la dirección.
ciudad = persona.get("dirección").get("ciudad")
print("Ciudad: ", ciudad)


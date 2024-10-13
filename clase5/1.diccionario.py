# Ejemplo de diccionario
diccionario_vacio = { }
print("Ejemplo de diccionario vacio: ", diccionario_vacio)

# Ejemplo basico de un diccionario, para definir una persona por ejemplo
persona = {         
    'nombre': 'Maria',   # Claves son atributos de la persona
    'edad': '30', 
    'casada': False, # Clave es string y el valor es booleano
    'hijos': ["Ana", "Luis"], # Clave es string y valor es una lista
    'direccion': {            # Clave es string y valor es un diccionario
        'calle':'La gran via'
    }
}

print("Ejemplo de diccionario basico: ", persona)

# Ejemplo de diccionario con valores de distintos tipos
diccionario_mixto = {
    'nombre': 'Alejandra',
    1: [2,3,4], #Clave es un entero y valor un string
    (2,3): 'tupla como clave' # Clave es una tupla y valor un string
}

print("Ejemplo de diccionario mixto: ", diccionario_mixto)

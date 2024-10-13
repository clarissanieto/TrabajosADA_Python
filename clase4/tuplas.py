# Crear una tupla con varios valores
tupla_mixta = (1, "hola", 3.5)

# Mostrar la tupla completa
print("Tupla completa: ", tupla_mixta)

# Acceder a los elementos de la tupla por su indice(posicion)
print("Primer elemento de la tupla: ", tupla_mixta[0])
print("Segundo elemento de la tupla: ", tupla_mixta[1])
print("Tercer elemento de la tupla: ", tupla_mixta[2])

# Explicación tuplas inmutables
print("\nLas tuplas no se pueden modificar. Intentemos modificar el primer elemento de la tupla")

# Ejemplo de intento de cambio que causaría error
# tupla_mixta[0] = 10 --> Type Error

# Explicación clara de la inmutabilidad
print("Si intentamos hacer 'tupla_mixta[0] = 10', Python mostrara por que no se puede cambiar ningun elemento de una tupla")

# Mostrar como si podemos "modificar" una tupla, creando una nueva tuplca
tupla_mixta = (10, "hola", 3.5)
print("Nueva tupla con el primer elemento cambiado: ", tupla_mixta)
print("Tupla original permanece sin cambios: ", tupla_mixta)


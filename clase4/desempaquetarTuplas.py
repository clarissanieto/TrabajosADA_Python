# Ejemplo 1: Desempaquetado basico de tuplas
# Crear una tupla con varios tipos de datos
mi_tupla = (1, "python", 3.14)
# Desempaquetar la tupla
numero, lenguaje, pi = mi_tupla
# Mostrar el valor de cada variable después del desempaquetado
print("Numero: ", numero)
print("Lenguaje: ", lenguaje)
print("Valor de Pi: ", pi)
# Deben de estar en orden las variables, deben de coincidir con los indices

# Ejemplo 2: Numero de variables no coincide con el numero de elementos
# Crear una tupla con 3 elementos
mi_tupla = (1, "python", 3.14)
# Intentar desempaquetar en dos varibles(esto causa error)
#numero, lenguaje = mi_tupla

# Ejemplo 3: Desempaquetado con el operador *
# Crear una tupla con varios elementos
mi_tupla = (1, "python", 3.14, "tuplas", "desempaquetado")
# Desempaquetar la tupla con el operador * para capturar varios elementos
primer_elemento, *resto = mi_tupla
# Mostrar los resultados del desempaquetado
print("\nPrimer elemento: ", primer_elemento)
print("Resto de los elementos: ", resto)

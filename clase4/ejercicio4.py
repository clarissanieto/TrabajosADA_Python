# Ejercicio 4: Manipulación de Tuplas y Comprobación de Índices
# • Crea una tupla llamada frutas con los siguientes elementos: ("manzana", "banana", "cereza").
frutas = ("manzana", "banana", "cereza")
print("Frutas: ", frutas)

# • Usa el método index para encontrar la posición de la fruta "banana".
posición_banana = frutas.index("banana")
print(f"La fruta banana se encuentra en la posición {posición_banana} de la tupla")

# • Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un mensaje indicando que no está presente.
fruta_buscada = "naranja"

if fruta_buscada in frutas: 
    print("La fruta naranja se encuentra dentro de la tupla")
else:
    print("La fruta naranja no se encuentra dentro de la tupla")

print("----------------------------------------------------------")

if "naranja" in frutas: # Sin definir en una variable "naranja"
    print("La fruta naranja se encuentra dentro de la tupla")
else:
    print("La fruta naranja no se encuentra dentro de la tupla")
    
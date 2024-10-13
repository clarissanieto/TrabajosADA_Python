# Escribe un programa que:
# 1. Itere sobre una lista de cadenas usando enumerate para mostrar el índice y el valor.
# 2. Utilice continue para saltar cadenas vacías.
# 3. Utilice break para detener la iteración si se encuentra una cadena con más de 5 caracteres.

lista = ["Liam", " ", "Zayn", "Harry", " ", "Niall", "Louis"]

for indice,nombre in enumerate(lista):
    if nombre == " ":
        continue 
    
    if len(nombre) < 5:
        print(f"Indice {indice}: {nombre}")
    else: 
        break


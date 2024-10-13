# Definir una función: parametros posicionales, con nombre y predeterminados
def presentar_persona(nombre, edad, ciudad="Desconocida", profesion="Desconocida"): 
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Profesion: {profesion}")
    print()
    
# Ejemplos de llamadas a la función

#Usando argumentos posiciones
print("Ejemplo con argumentos posiciones: ")
presentar_persona("Ana", 30)

# Usando argumentos posicionales y con nombre (sustituye los valores que ya habíamos definido en la función)
print("Ejemplo con argumentos posiciones y con nombre: ")
presentar_persona("Luis", 25, ciudad="Madrid", profesion="Ingeniero")

# Usando todos los argumentos con nombre
print("Ejemplo de todos los argumentos con nombre: ")
presentar_persona(nombre="Martha", edad=25, ciudad="Madrid", profesion="Ingeniera")



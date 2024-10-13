# Programación para adivinar un numero secreto
# Definir el numero secreto
num_secreto = 7 

# Inicializar la variable para almacenar el numero del usuario
numero_adivinado = None 

# Mensaje inicial
print("Adivina el numero secreto (entre el 1 y el 10): ")

# Bucle while que continua hasta que el usuario adivine el numero secreto
while numero_adivinado != num_secreto:
    #Solicitar al usario que ingrese un numero
    numero_adivinado = int(input("Introduce tu numero: "))
    
    # Comprobar si el numero adivinado es correcto
    if numero_adivinado < num_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif numero_adivinado > num_secreto:
        print("Demasiado alto. Intenta de nuevo")
    else:
        print("Felicidades!! Has adivinado el numero secreto!")

# Mensaje de finalización del juego
print("Gracias por jugar!")

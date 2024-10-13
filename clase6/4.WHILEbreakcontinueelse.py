# Programa que pide numero hasta que se ingrese un numero negativo

# Inicializamos la variable suma para acumular la suma de los 
# numeros positivos

suma = 0 # variable de suma vacia, donde se iran sumando todos los numeros que se vayana agregando

# Inializamos un ciclo infinito usando while true
while True:
    # Solicitamos al usuario que introduzca un numero
    # La entrada se convierte en numero entero
    entrada = int(input("Introduce un numero (negativo para terminar): "))
    
    # Verificamos si el numero ingresado es negativo
    if entrada  < 0:
        # Si el numero es negativo, salimos del diclo usando 
        break
    
    #Sumamos el numero positivo ingresado a la variable suma
    suma += entrada 
    
    #Verificar si el numero ingresado es par
    if entrada % 2 == 0:
        #Si el numero es par, usamos continue para saltar la impresión
        # y pasar a la siguiente iteracion del ciclo
        continue
    # si el numero ingresado no es par, se ejecuta esta linea:
    print(f"Numero impar ingresado: {entrada}")

else:
    print(f"El ciclo ha terminado por que se ingreso un numero negativo")
    
# Mensaje final
print(f"La suma de los numeros ingresados es: {suma}")

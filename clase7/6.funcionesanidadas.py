# Ejemplo 1: basico funciones anidadas
def funcion_externa(x):
    def funcion_interna(y):
        return y + 10
    return funcion_interna(x) # Llamada a la funcion interna con el parametro x

# Llamada a la funcion externa
resultado = funcion_externa(5)
print(f"Resultado de la funcion_externa(5): {resultado}")

# Ejemplo 2: Closure
def crear_mutiplicador(factor):
    def multiplicar(x):
        return x * factor
    return multiplicar 
duplicar = crear_mutiplicador(2)
triplicar =  crear_mutiplicador(3)

print(f"Duplicar 10: {duplicar(10)}")
print(f"triplicar 10: {triplicar(10)}")


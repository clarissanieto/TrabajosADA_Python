# Lista inicial
mi_lista = [10, 20, 30, 40, 50]
print("Lista original: ", mi_lista)

# Actualizar un elemento en especifico
mi_lista[2] = 35
print("Lista después de actualizar el tercer elemento: ", mi_lista)

# Actualizar un elemento usando indices negativos
mi_lista[-1] = 60
print("Lista despues de actualizar el ultimo elemento: ", mi_lista)

# Actualizar varios elementos usando slicing
mi_lista[1:4] = [25,35,45]
print("Lista después de actualizar un rango de elementos: ", mi_lista)

# Actualizar basado en una condición
for i in range(len(mi_lista)):
    if mi_lista[i] > 30:
        mi_lista[i] += 10
print("Lista después de actualizar elementos mayores que 30: ", mi_lista)

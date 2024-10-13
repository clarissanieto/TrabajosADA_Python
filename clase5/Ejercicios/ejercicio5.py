# Ejercicio 5: Diccionario dentro de una Lista 
# 1. Crea una lista de diccionarios donde cada diccionario representa un producto en una tienda, con claves: 
# o Nombre 
# o Precio 
# o Cantidad en stock 

producto_tienda = [{"Nombre":"Café", "Precio": 80, "Cantidad en stock": 100}, 
                   {"Nombre": "Pan bolillo", "Precio": 4, "Cantidad en stock":40},
                   {"Nombre": "Leche", "Precio": 70, "Cantidad en stock": 50}]

print(producto_tienda)

# 2. Imprime el nombre y el precio del segundo producto en la lista. 

segundo_producto = producto_tienda[1]
nombre = segundo_producto["Nombre"]
precio = segundo_producto["Precio"]

print("El segundo producto es: ", nombre)
print(f"El segundo producto tiene un precio de {precio} pesos mexicanos")

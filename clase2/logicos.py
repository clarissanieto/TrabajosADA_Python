# Definimos distintas variables para usar en las comparaciones
a = 10
b = 5
c = 15
d = 8 

# Operador AND
resultado_and = (a > b) and (c > d)
print(f"Resultado de (a >b) and (c > d): {resultado_and}")
# Ambas condiciones deben ser verdaderas para que el resultado sea TRUE
# (a > b) es True por que 10 > 5
# (c > d) es True por que 15 > 8

# Operador OR
resultado_or = (a < b) or (c > d)
print(f"Resultado de (a < b) or (c > d): {resultado_or}")
# Al menos una de las condiciones debe ser verdadera para que el resultado sea TRUE
# (a < b) = False, por que 10 no es menor que 5
# (c > d) = True, por que 15 es mayor que 8

# Operador NOT
resultado_not = not (a < b)
print(f"Resultado de not (a < b): {resultado_not}")
# El operador NOT invierte el valor de la expresión
# Por lo tanto, (a < b) es false por que 10 no es menor que 5, pero NOT false es TRUE

# Combinación de los operadores logicos AND, OR y NOT en una sola expresion
resultado_combinado = (a > b) and (not (c < d)) or (b < c)
print(f"Resultado combinado: {resultado_combinado}")
# (a > b) es True por que 10 > 5 
# (c < d) es False por que 15 no es menor que 8, y Not false resulta en TRUE
# (a > b) and (c < d) es True por que True and True es True
# True and True resulta en True
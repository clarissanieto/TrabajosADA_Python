# Importamos el modulo completo
# No importa en que carpeta está el modulo, puede ser la misma o diferente, se podrá importar
import operaciones
print(f"Suma(import completo): {operaciones.sumar(2,3)}")
# operaciones.sumar = invocamos al modulo y a la función y agregamos los parametros para que corra la función

# Renombrar el modulo
import operaciones as op
print(f"Resta(modulo renombrado): {op.restar(5,2)}")

# Importar una funcion especifica
from operaciones import multiplicar
print(f"Multiplicacion con una funcion especifica): {multiplicar(3,2)}")

# Renombramos una funcion especifica
from operaciones import sumar as suma
print(f"Suma(con una funcion renombrada): {suma(10,70)}")

# Importar todo el modulo con *
from operaciones import * 
print(f"Resta (import *): {restar(30, 5)}")

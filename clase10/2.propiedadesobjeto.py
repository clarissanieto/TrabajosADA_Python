# 2. Propiedades de un objeto

# Definir la clase persona

class Persona:
    def __init__(self, nombre, edad):
        # Iniciar las propiedes del objeto
        self. nombre= nombre
        self. edad =  edad 

# Crear objeto de la clase persona
persona1 = Persona("Ana", 20)
persona2 = Persona("Luis", 35)
# Acceder a las propiedades del objeto
print(persona1.nombre)
print(persona1.edad)

print(persona2.nombre)
print(persona2.edad)

# La clase persona define un objeto que tiene propiedades como nombre y edad
# Al instanciar persona1 con valores especificos, se crean atributos unicos que representan 
# el estado de ese objeto
# Se puede acceder a las propiedades utilizando la notacion de punto, lo que permire 
# obtener informacion sobre la isntancia creada



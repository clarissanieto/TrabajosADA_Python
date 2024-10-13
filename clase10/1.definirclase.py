# Definir clase en Python

# Definimos clase llamada coche
class Coche: 
    # Metodo __init__ es el constructor que se llama al crear un nuevo objeto
    def __init__(self, marca, modelo): 
        # Self es una referencia al objeto que estamos creando
        # Iniciamos los atributos de la instancia
        self.marca =  marca # Atributo de instancia: guarda la marca del coche
        self.modelo = modelo # Atributo de instancia: guarda el modelo del coche
# La clase Coche es una plantilla para crear objetos de tipo auto.
# Contiene un metodo constructor __init__ que inicia los atributos especificos de cada coche
# Como por ejemplo: marca, modelo usando la referencia self para distinguir entre las propiedades del objeto y los parametros pasados al constructor


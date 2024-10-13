# 4. Atributos de Instancia

# Definimos la clase 
class Gato:
    def __init__(self, color, nombre):
        self.color =  color # Atributo de instancia
        self.nombre = nombre

# Crear diferetes objetos (instancias) de la clase Gato
gato1 = Gato("negro", "Felix")
gato2 = Gato("gris", "Ares")

# Acceder a los atributos de instancia
print(gato1.color)
print(gato2.color)

# La clase gato incluye atributos de instancia como color y nombre, que se inicializan en el constructor
# Cada objeto creado a partir de esta clase (como gato1 y gato2) tienen sus propios valorespata estos atributos
# lo que permite que diferentes instancias representen gatos distintos con caracteristicas unicas.

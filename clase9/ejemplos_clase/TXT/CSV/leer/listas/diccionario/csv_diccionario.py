# Importar modulo
import csv

# Abrir el archivo csv en modo lectura
with open("archivo2.csv", "r") as file:
    # Creamos el lector de diccionario que porcesa un archivo csv
    # El lector convierto cada fila en un diccionario usando los
    # encabezados de columnas como claves
    reader = csv.reader(file)
    
    # Iterar sobre cada fila del archivo csv
    for fila in reader:
        print(fila)
        # Imprimimos cada fila como diccionario
        
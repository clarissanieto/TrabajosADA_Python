import os # Importar modulo

# Definir el nombre del archivo
nombre_archivo = 'archivo.txt'

# Comprobar si el archivo existe en la ruta especificada
# La funcion os.path. exists() devuelve True si el archivo existe y False en caso contrario
if os.path.exists(nombre_archivo):
    # Si el archivo existe, procederá a eliminarlo 
    # La funcion os.remove() elimina el archivo en la ruta especifica
    os.remove(nombre_archivo)
    print(f"Archivo {nombre_archivo} eliminado")
else: 
    # Si el archivo no existe, informar al usuario que no se encontró nada
    print(f"El archivo {nombre_archivo} no existe")
    

# Los 3 ejemplos de escritura (TXT)

# Modo 'w': sobreescribe el archivo
with open('modo_w.txt', 'w') as file: 
    file.write("Este archivo fue sobreescrito por el modo \ 'w\'.\n")
    file.write("Todo el contenido previo fue eliminado")
print("Archivo 'modo_w.txt' creadp con exito")

# Modo 'a': agrega contenido al archivo existente
with open('modo_w.txt', 'a') as file: 
    file.write("Este archivo se le agregó al final con \ 'a\'.\n")
    file.write("Todo el contenido previo no fue eliminado")
print("Archivo 'modo_w.txt' creado/modificado con exito")

# Modo 'x': Crea un nuevo archivo
with open('modo_x.txt', 'a') as file: 
    file.write("Este archivo fue creado con existo usando \ 'x\'.\n")
    file.write("Falla si ya existe el archivo")
print("Archivo 'modo_x.txt' creado con exito")


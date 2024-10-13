import os

class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property 
    def nombre(self):
        return self.__nombre

class CatalogoPelicula:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt"
        self._crear_catalogo_si_no_existe()

    def _crear_catalogo_si_no_existe(self):
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w') as archivo:
                pass  # Solo crear el archivo vacío

    def agregar(self, pelicula):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(pelicula.nombre + '\n')

    def listar(self):
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'r') as archivo:
                peliculas = archivo.readlines()
                return [pelicula.strip() for pelicula in peliculas]
        return []

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)

def menu(catalogo):
    while True:
        print("\nMenú de Opciones:")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar Catálogo de Películas")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar(pelicula)
            print(f"Película '{pelicula.nombre}' agregada al catálogo.")
        
        elif opcion == '2':
            print("Películas en el catálogo:")
            peliculas = catalogo.listar()
            if peliculas:
                for p in peliculas:
                    print(f"- {p}")
            else:
                print("No hay películas en el catálogo.")
        
        elif opcion == '3':
            confirmacion = input("¿Está seguro de que desea eliminar el catálogo? (sí/no): ")
            if confirmacion.lower() == 'si':
                catalogo.eliminar()
                print("Catálogo de películas eliminado.")
                break
        
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, intenta nuevamente.")

def main():
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
    catalogo = CatalogoPelicula(nombre_catalogo)
    menu(catalogo)

if __name__ == "__main__":
    main()




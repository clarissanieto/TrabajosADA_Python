# Ejercicio 7: Contar Ocurrencias de Elementos en un Diccionario Anidado 
# 1. Crea un diccionario que contenga información sobre tres clubes deportivos, cada uno con una lista de jugadores. 
# o Cada jugador es un diccionario con las claves: nombre y edad. 

clubes_deportivos = {
    "Club de Tenis": [
        {"Nombre": "Menganito", "Edad": 20},
        {"Nombre": "Menganita", "Edad": 21}, 
        {"Nombre": "Menganite", "Edad": 21}
    ], 
    "Club de Volleyball": [
        {"Nombre": "Fulanito", "Edad": 23},
        {"Nombre": "Fulanita", "Edad": 22}, 
        {"Nombre": "Fulanite", "Edad": 25}
    ],
    "Club de Beisball": [
        {"Nombre": "Juanchito", "Edad": 25}, 
        {"Nombre": "Juanchita", "Edad": 24}, 
        {"Nombre": "Juanchite", "Edad": 22}
    ]
}

# 2. Cuenta cuántos jugadores en total tienen cada uno de los clubes 

club_tenis = clubes_deportivos["Club de Tenis"]
cantidad_jugadores_tenis = len(clubes_deportivos)
print(f"El Club de Tenis tiene {cantidad_jugadores_tenis} jugadores en total")

club_volleyball = clubes_deportivos["Club de Volleyball"]
cantidad_jugadores_volleyball = len(club_volleyball)
print(f"El Club de Volleybal tiene {cantidad_jugadores_volleyball} jugadores en total")

club_beisball = clubes_deportivos["Club de Beisball"]
cantidad_jugadores_beisball = len(club_beisball)
print(f"El Club de Beisball tiene {cantidad_jugadores_beisball} jugadores en total")



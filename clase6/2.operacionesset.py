# Craer conjuntos
conjunto_a = {1,2,3,4}
conjunto_b = {3,4,5,6}
conjunto_c = {7,8,9}

# Subconjunto
es_subconjunto = conjunto_a.issubset(conjunto_b)
print(f"Es conjunto_a un subjuntos de conjunto b: {es_subconjunto}")

# Super conjunto
es_superconjunto = conjunto_b.issuperset(conjunto_a)
print(f"Es conjunto_b un superconjunto de conjunto_a?: {es_superconjunto}")

# Disconjuntos
son_disconjuntos = conjunto_a.isdisjoint(conjunto_c)
print(f"Son conjunto_a y conjunto_c disjuntos?: {son_disconjuntos}")

# Simetría
simetria = conjunto_a.symmetric_difference(conjunto_b)
print(f"Diferencia simetrica entre conjunto_a y conjunto_b: {simetria}")

# Union update
conjunto_a.update(conjunto_b)
print(f"Conjunto_a después de la union con conjunto_b: {conjunto_a}")

# Interseccion Update
conjunto_a.intersection_update(conjunto_b)
print(f"conjunto_a después de la intersección con conjunto_b: {conjunto_a}")

# Difference Update
conjunto_b.difference_update(conjunto_c)
print(f"Conjunto_b después de la diferencia con conjunto_c: {conjunto_c}")


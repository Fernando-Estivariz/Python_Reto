def nombres_con_a(nombres):
    return [nombre for nombre in nombres if nombre.startswith('A')]

nombres = ["Angel", "Cecilia", "Daniel", "Alvaro", "Ana"]
nombres_a = nombres_con_a(nombres)
print("Nombres que comienzan con 'A':", nombres_a)

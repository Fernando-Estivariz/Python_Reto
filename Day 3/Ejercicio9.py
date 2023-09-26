def contar_palabras_largas(palabras):
    return sum(1 for palabra in palabras if len(palabra) > 5)

palabras = ["papaya", "platano", "piña", "sandía", "durazno"]
contador = contar_palabras_largas(palabras)
print("Cantidad de palabras con más de cinco caracteres:", contador)

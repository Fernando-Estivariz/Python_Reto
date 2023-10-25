def encontrar_longitud_palabra_mas_larga(oracion):
    palabras = oracion.split()  # Dividir la oración en palabras
    longitud_palabra_mas_larga = 0

    for palabra in palabras:
        # Eliminar signos de puntuación y contar la longitud de cada palabra
        longitud_palabra = len(palabra.rstrip(".,!?"))
        if longitud_palabra > longitud_palabra_mas_larga:
            longitud_palabra_mas_larga = longitud_palabra

    return longitud_palabra_mas_larga

# Ejemplo de uso del programa
oracion = "Esta es una oración de ejemplo con palabras más largas como 'elefante' y 'anticonstitucionalidad'."
longitud = encontrar_longitud_palabra_mas_larga(oracion)
print(f"La longitud de la palabra más larga en la oración es: {longitud}")

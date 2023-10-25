def oracion_invertida(oracion):
    # Divide la oración en palabras
    palabras = oracion.split()
    # Invierte el orden de las palabras
    palabras_invertidas = palabras[::-1]
    # Reconstruye la oración invertida
    oracion_invertida = ' '.join(palabras_invertidas)
    return oracion_invertida

# Ejemplo de uso de la función
oracion_original = "Esta es una oración de ejemplo para ser invertida."
invertida = oracion_invertida(oracion_original)
print("Oración original:", oracion_original)
print("Oración invertida:", invertida)

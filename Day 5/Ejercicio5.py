def eliminar_vocales(cadena):
    vocales = "AEIOUaeiou"
    # Usa una comprensión de lista para filtrar las vocales
    cadena_modificada = "".join([caracter for caracter in cadena if caracter not in vocales])
    return cadena_modificada

# Ejemplo de uso de la función
cadena = "Esta es una cadena de ejemplo con vocales"
resultado = eliminar_vocales(cadena)
print("Cadena original:", cadena)
print("Cadena modificada:", resultado)

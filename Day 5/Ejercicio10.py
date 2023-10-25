def palabra_presente_en_oracion(oracion, palabra):
    # Convertimos tanto la oración como la palabra a minúsculas para realizar una búsqueda que no distinga entre mayúsculas y minúsculas.
    oracion = oracion.lower()
    palabra = palabra.lower()

    # Verificamos si la palabra está en la oración
    if palabra in oracion:
        return True
    else:
        return False

# Ejemplo de uso del programa
oracion = "Esta es una oración de ejemplo para probar el programa."
palabra = "ejemplo"
resultado = palabra_presente_en_oracion(oracion, palabra)

if resultado:
    print(f"La palabra '{palabra}' está presente en la oración.")
else:
    print(f"La palabra '{palabra}' no está presente en la oración.")

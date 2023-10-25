import string

def es_pangrama(cadena):
    # Convierte la cadena a minúsculas para que no distinga entre mayúsculas y minúsculas
    cadena = cadena.lower()
    # Define un conjunto de letras presentes en la cadena
    letras = set(char for char in cadena if char.isalpha())
    # Compara el conjunto de letras con el alfabeto español completo
    alfabeto_espanol = set("abcdefghijklmnñopqrstuvwxyz")
    return alfabeto_espanol <= letras

# Ejemplo de uso de la función
cadena = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja."
resultado = es_pangrama(cadena)
print(f"¿La cadena es un pangrama en español? {resultado}")


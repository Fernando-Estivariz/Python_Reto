def contar_nombres_con_vocal(lista_de_nombres):
    vocales = "AEIOUaeiou"
    contador = 0

    for nombre in lista_de_nombres:
        if nombre[0] in vocales:
            contador += 1

    return contador

# Ejemplo de uso de la función
nombres = ["Ana", "Carlos", "Eva", "Olivia", "Isabel", "Ursula"]
conteo = contar_nombres_con_vocal(nombres)
print(f"La cantidad de nombres que comienzan con una vocal es: {conteo}")

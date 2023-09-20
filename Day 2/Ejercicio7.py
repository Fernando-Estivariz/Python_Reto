# Lista de números enteros
numeros = [-8, -2, 19, 11, 7, 13]

# Inicializar la suma de números positivos
suma_positivos = 0

# Iterar a través de la lista y sumar los números positivos
for numero in numeros:
    if numero > 0:
        suma_positivos += numero

print(f"La suma de los números positivos es: {suma_positivos}")




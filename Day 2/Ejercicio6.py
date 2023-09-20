# Pedir al usuario que ingrese una cantidad de días
dias1 = int(input("Ingresa una cantidad de días: "))

# Calcular años, semanas y días
años, dias = divmod(dias1, 365)
semanas, dias = divmod(dias1, 7)

# Mostrar el resultado
print(f"{dias1} días equivalen a {años} años, {semanas} semanas y {dias} días restantes")

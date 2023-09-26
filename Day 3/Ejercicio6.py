def tabla_de_multiplicar(numero, multiplicador=1):
    if multiplicador > 10:
        return
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    tabla_de_multiplicar(numero, multiplicador + 1)

numero = int(input("Ingresa un número para la tabla de multiplicar: "))
tabla_de_multiplicar(numero)

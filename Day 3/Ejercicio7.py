def factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos"
    if numero == 0:
        return 1
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Ingresa un número: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

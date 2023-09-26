def suma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

numero = int(input("Ingresa un número: "))
resultado = suma_digitos(numero)
print(f"La suma de dígitos de {numero} es {resultado}")

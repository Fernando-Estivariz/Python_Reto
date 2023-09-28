def imprimir_mensaje_o_numero(numero):
    if isinstance(numero, (int, float)):
        print(f"El número ingresado es: {numero}")
    else:
        print("Entrada no válida. Por favor, proporcione un número válido.")

numero = 42
imprimir_mensaje_o_numero(numero)

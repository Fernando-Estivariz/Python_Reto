def reverse_string(input_string):
    # Utiliza la rebanada [::-1] para revertir la cadena
    reversed_string = input_string[::-1]
    return reversed_string

# Ejemplo de uso de la función
input_string = "Fernando Estivariz"
reversed = reverse_string(input_string)
print(reversed)

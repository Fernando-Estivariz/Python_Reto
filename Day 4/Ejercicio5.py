def verificar_par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

num = 7
resultado = verificar_par_o_impar(num)
print(f"{num} es un número {resultado}.")

def palindromo(cadena):
    # Eliminamos los espacios en blanco y convertimos la cadena a minusculas
    cadena = cadena.replace(" ", "").lower()
    
    # Inicializamos índices para recorrer la cadena desde ambos extremos
    inicio = 0
    fin = len(cadena) - 1
    
    # Comparamos los caracteres desde ambos extremos hacia el centro
    while inicio < fin:
        if cadena[inicio] != cadena[fin]:
            return False
        inicio=inicio+1
        fin -= 1
    
    return True

cadena = "Anilina"
if palindromo(cadena):
    print("La cadena es un palindromo.")
else:
    print("La cadena no es un palindromo.")

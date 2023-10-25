def eliminar_duplicados(cadena):
    # Creamos una cadena vacía para almacenar el resultado
    cadena_resultado = ""
    
    for caracter in cadena:
        if caracter not in cadena_resultado:
            cadena_resultado += caracter
            
    return cadena_resultado

# Ejemplo de uso de la función
cadena_original = "programación"
resultado = eliminar_duplicados(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena con duplicados eliminados:", resultado)

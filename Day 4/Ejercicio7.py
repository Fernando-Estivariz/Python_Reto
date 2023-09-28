def ordenar_lista_alfabeticamente(lista_de_colores):
    # Utiliza la función sorted() para ordenar la lista alfabéticamente
    lista_ordenada = sorted(lista_de_colores)
    return lista_ordenada

# Ejemplo de uso:
colores = ["Rojo", "Verde", "Azul", "Amarillo", "Blanco"]
lista_ordenada = ordenar_lista_alfabeticamente(colores)
print("Lista original:", colores)
print("Lista ordenada alfabéticamente:", lista_ordenada)

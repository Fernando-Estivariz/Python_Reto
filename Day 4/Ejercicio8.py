def encontrar_interseccion(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    
    interseccion = set1 & set2
    
    lista_interseccion = list(interseccion)
    
    return lista_interseccion

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
resultado = encontrar_interseccion(lista1, lista2)
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Intersección:", resultado)

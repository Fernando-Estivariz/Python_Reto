def square_elements(input_list):
    squared_list = [x**2 for x in input_list]
    return squared_list

# Ejemplo de uso:
input_list = [1, 2, 3, 4, 5]
result = square_elements(input_list)
print("Lista original:", input_list)
print("Cuadrados de los elementos:", result)

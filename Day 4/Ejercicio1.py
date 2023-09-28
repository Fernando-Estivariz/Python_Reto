def sum_of_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    
    sum_positive = sum(positive_numbers)

    return sum_positive

numbers = [1, 2, 3, -4, -5, 6, -7]
result = sum_of_positive_numbers(numbers)
print("La suma de los números positivos es:", result)

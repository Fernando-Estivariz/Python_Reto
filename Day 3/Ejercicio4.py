def fibonacci_recursivo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci_recursivo(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

n_terminos = int(input("Número de términos en la secuencia de Fibonacci: "))
resultado = fibonacci_recursivo(n_terminos)
print("Secuencia de Fibonacci:", resultado)

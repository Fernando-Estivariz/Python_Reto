def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]

input_str = "racecar"
if is_palindrome(input_str):
    print(f"'{input_str}' es un palíndromo.")
else:
    print(f"'{input_str}' no es un palíndromo.")

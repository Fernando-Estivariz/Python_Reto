def count_words_in_sentence(sentence):
    # Divide la oración en palabras utilizando el espacio como separador
    words = sentence.split()
    # Cuenta el número de palabras
    word_count = len(words)
    return word_count

# Solicitar una oración al usuario
input_sentence = input("Por favor, ingresa una oración: ")

count = count_words_in_sentence(input_sentence)
print(f"El número de palabras en la oración es: {count}")

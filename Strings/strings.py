def palindrome(word):
    reverse_letters = []

    for letter in word:#hasta que termine la palabra
        reverse_letters.insert(0, letter)#inserta la letra en la posicion 0 del arreglo
    reversed_word = ''.join(reverse_letters)# Une el arreglo en un string
    #en python3 si se puede modificar str
    if reversed_word == word:
        return True
    return False

def palindrome2(word):
    reversed_word = word[::-1]#con pasos de -1 hace de atras hacia adelante

    if reversed_word == word:
        return True
    return False

if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))

    result = palindrome2(word)

    if result is True:
        print('{} sí es un palíndromo'.format(word))
    else:
        print('{} no es un palíndromo'.format(word))
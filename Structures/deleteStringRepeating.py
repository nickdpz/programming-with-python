"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
    seen_letters = {}#diccionario ejemplo a : 3 

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)#solo la ha visto 1 vez
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    for key, value in seen_letters.items():#itera el diccionario
        if value[1] == 1:
            final_letters.append( (key, value[0]) )#añade al incio del arreglo
            #lista de tuplas [(a,0),(b,5)]
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])#ordena una lista con forme al indice, con una lambda

    if not_repeated_letters:
        return not_repeated_letters[0][0] # retorna primer valor de la lista osea la tupla con la letra
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)#crea una tupla

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        #importante
        print('El primer caracter no repetido es: {}'.format(result))
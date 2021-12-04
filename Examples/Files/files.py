def write():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

def read():
    counter = 0
    with open('aleph.txt') as f:#guarda el contenido del archivo como f
        for line in f:
            counter += line.count('Beatriz')

    print('Beatriz se encuentra {} en el texto'.format(counter))


if __name__ == '__main__':
    write()
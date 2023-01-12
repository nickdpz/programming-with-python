n = 100
listE = []
while (n > 0):
    listE.append(n % 2 == 0)
    n = int(n/2)
while (len(listE)):
    print(listE.pop())

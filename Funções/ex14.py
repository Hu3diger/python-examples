import random
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
boolean = False
def quadrado_magico():
    global boolean
    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        boolean = True
    else:
        boolean = False
    return boolean
while boolean == False:
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            choice = random.choice(vetor)
            matriz[i][j] = choice
            indice = vetor.index(choice)
            vetor = vetor[:indice] + vetor[indice + 1:]
    quadrado_magico()
    print("\n", matriz[0], "\n", matriz[1], "\n", matriz[2])
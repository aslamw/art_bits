from array import array

# Defina o número de linhas e colunas
num_linhas = 3
num_colunas = 4

# Crie uma lista de arrays vazios para representar a matriz
matriz = [array('i', [0] * num_colunas) for _ in range(num_linhas)]
matriz[0][1] = 1
# Para ilustrar a matriz:
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()

for linha in matriz:
    if 2 in linha:
        print('ok 2')
        break
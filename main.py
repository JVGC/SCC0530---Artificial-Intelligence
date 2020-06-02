# Usage: python3 trab3.py
# Entrada do programa: nome do arquivo
#	ex: entrada.txt 
# Saida do programa: posicoes percorridas e numero de passos
#
from Search import best_first_search, DFS

# Checa se um vizinho deve ser adicionado na lista de abertos

maze = {}
# Adiciona um caracter qualquer para iniciar o loop
chars = ['c']
start = None
end = None
heightMaze = 0
fileName = input("Digite o nome do arquivo: ")

# Abre o arquivo
fp = open(fileName, 'r')

# Faz a leitura do comeco do arquivo pegando altura e largura
height = fp.read(2)
fp.read(1) 
width = fp.read(2)
# Uma leitura a mais para pegar o '\n' no arquivo
fp.readline()

while len(chars) > 0:
    # Pega os caracteres de uma linha do arquivo
    chars = [str(i) for i in fp.readline().strip()]

    # Adiciona os caracteres no maze
    for x in range(len(chars)):
        maze[(heightMaze, x)] = chars[x]
        # Caso for o ponto de partida, adiciona no start
        if(chars[x] == '#'):
            start = (heightMaze, x)
        # Caso for o ponto de chegada, adiciona no end
        elif(chars[x] == '$'):
            end = (heightMaze, x)

    # Incrementa a altura da matriz na leitura
    if(len(chars) > 0):
        heightMaze += 1

# Fecha o arquivo após uso 
fp.close()

# Encontra o menor caminho a partir de '#', indo até '$'
path = best_first_search(maze, start, end)
print('Best_first Search')
print('Posições percorridas: ')
print(path)
print()
print('Passos até o objetivo: {0}'.format(len(path)))
print()
path = DFS(maze, start, end, int(height), int(width))

print('DFS')
print('Posições percorridas: ')
print(path)
print()
print('Passos até o objetivo: {0}'.format(len(path)))
print()
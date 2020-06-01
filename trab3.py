# Usage: python3 trab3.py
# Entrada do programa: nome do arquivo
#	ex: entrada.txt 
# Saida do programa: posicoes percorridas e numero de passos
#

class Node:

    # Inicializacao da classe
    def __init__(self, position:(), parent:()):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance do nó inicial
        self.h = 0 # Distancia do nó objetivo
        self.f = 0 # Custo total calculado

    # Compara os nós
    def __eq__(self, other):
        return self.position == other.position

    # Ordenação dos nós
    def __lt__(self, other):
         return self.f < other.f

    # Formatação da saída dos nós
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

# Best-first search
def best_first_search(maze, start, end):
    
    # Cria lista dos nós abertos e dos nós fechados
    open = []
    closed = []

    # Cria um nó inicial e um nó objetivo
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Adiciona o nó incial na lista de abertos
    open.append(start_node)
    
    # Loop até que a lista de abertos esteja vazia
    while len(open) > 0:

        # Ordena a lista de nós abertos para encontrar o nó com menor custo
        open.sort()

        # Pega o nó com menor custo que se encontra no inicio
        current_node = open.pop(0)

        # Adiciona o nó na lista de fechados
        closed.append(current_node)
        
        # Checa se o objetivo foi atingido
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # Pega a posicao do nó no labirinto
        (x, y) = current_node.position

        # Obtem os vizinhos do nó
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        # Loop entre os vizinho para obter proximo nó
        for next in neighbors:

            # Pega o char do labirinto
            maze_value = maze.get(next)

            # Caso for uma parede, ir para proxima iteração
            if(maze_value == '-'):
                continue

            # Cria um nó do vizinho
            neighbor = Node(next, current_node)

            # Se o vizinho ja foi visitado, ir para proxima iteracao
            if(neighbor in closed):
                continue

            # Gera heurística para obter custo total (Distancia Manhattan)
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.h

            # Checa se o vizinho esta na lista de aberto e se tem um custo total inferior ao atual
            if(add_to_open(open, neighbor) == True):
                # Adiciona o vizinho na lista de abertos
                open.append(neighbor)

    # Return None, se nenhum caminho foi encontrado
    return None

# Checa se um vizinho deve ser adicionado na lista de abertos
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True

def main():

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
	width = fp.read(2)
	fp.read(1) 
	height = fp.read(2)
	# Uma leitura a mais para pegar o '\n' no arquivo
	fp.readline()

	while len(chars) > 0:
		# Pega os caracteres de uma linha do arquivo
		chars = [str(i) for i in fp.readline().strip()]

		# Adiciona os caracteres no maze
		for x in range(len(chars)):
			maze[(x, heightMaze)] = chars[x]
			# Caso for o ponto de partida, adiciona no start
			if(chars[x] == '#'):
				start = (x, heightMaze)
			# Caso for o ponto de chegada, adiciona no end
			elif(chars[x] == '$'):
				end = (x, heightMaze)

		# Incrementa a altura da matriz na leitura
		if(len(chars) > 0):
			heightMaze += 1

	# Fecha o arquivo após uso 
	fp.close()

	# Encontra o menor caminho a partir de '#', indo até '$'
	path = best_first_search(maze, start, end)
	print('Posições percorridas: ')
	print(path)
	print()
	print('Passos até o objetivo: {0}'.format(len(path)))
	print()

if __name__ == "__main__": main()
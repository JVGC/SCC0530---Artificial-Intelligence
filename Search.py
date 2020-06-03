from Node import Node, add_to_open

# Best-first search
def Best_First_Search(maze, start, end):
    
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

def visit(maze, current_node, goal_node, visited):
    
    visited.append(current_node)
    
    x, y = current_node.position
    neighbors = []
    
    if(x != 0 ):
        neighbors.append((x-1,y))
    if(x < maze['height']-1 ):
        neighbors.append((x+1,y))
    if(y != 0 ):
        neighbors.append((x,y-1))
    if(y < maze['width']-1 ):
        neighbors.append((x,y+1))
    
    for i in neighbors:
        maze_value = maze.get(i)
        
        if(maze_value == '-'):
            continue
        
        neighbor = Node(i, current_node)
        
        if(neighbor in visited):
            continue
            
        if(neighbor == goal_node):
            return neighbor
        
        temp = visit(maze, neighbor, goal_node, visited)
        if temp is not None:
            return temp
    
    return None

def Depth_First_Search(maze, start, end):
    
    visited = []
    
    start_node = Node(start, None)
    goal_node = Node(end, None)
    goal_node = visit(maze, start_node, goal_node, visited)
    
    path = []
    while goal_node != start_node:
        path.append(goal_node.position)
        goal_node = goal_node.parent
    return path[::-1]

def Breadth_First_Search(maze, start, end):
    # Cria lista dos nós abertos e dos nós fechados
    open = []
    closed = []
    neighbors = []

    # Cria um nó inicial e um nó objetivo
    start_node = Node(start, None)
    goal_node = Node(end, None)

    # Checa se o objetivo foi atingido
    if start_node == goal_node:
        path = [start_node]
        return path


    # Adiciona o nó incial na lista de abertos
    open.append(start_node)
    
    # Loop até que a lista de abertos esteja vazia
    while len(open) > 0:

        # Pega o nó com menor custo que se encontra no inicio
        current_node = open.pop(0)

        # Adiciona o nó na lista de fechados
        closed.append(current_node)
        
        # Pega a posicao do nó no labirinto
        (x, y) = current_node.position
        
        # Obtem os vizinhos do nó
        if(x > 0 ):
            neighbors.append((x-1,y))
        if(x < maze['height']-1 ):
            neighbors.append((x+1,y))
        if(y > 0 ):
            neighbors.append((x,y-1))
        if(y < maze['width']-1 ):
            neighbors.append((x,y+1))

        # Loop entre os vizinho para obter proximo nó
        for i in neighbors:

            # Pega o char do labirinto
            maze_value = maze.get(i)

            # Caso for uma parede, ir para proxima iteração
            if(maze_value == '-'):
                continue

            # Cria um nó do vizinho
            neighbor = Node(i, current_node)

            # Se o vizinho ja foi visitado, ir para proxima iteracao
            if(neighbor in closed):
                continue
            
            if neighbor == goal_node:
                path = []
                while neighbor != start_node:
                    path.append(neighbor.position)
                    neighbor = neighbor.parent
                return path[::-1]

            open.append(neighbor)
        
        neighbors.clear()

    # Return None, se nenhum caminho foi encontrado
    return None
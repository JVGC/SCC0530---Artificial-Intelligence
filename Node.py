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

def add_to_open(open, neighbor):
        for node in open:
            if (neighbor == node and neighbor.f >= node.f):
                return False
        return True

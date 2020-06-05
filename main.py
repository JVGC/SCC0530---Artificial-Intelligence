'''
Usage: python3 main.py

Input: name of file with the information of the maze, ex: input.txt

Output: Path found and number of steps for each of the algorithms
'''

from Search import best_first_search, depth_first_search, breadth_first_search, astar_search, simple_hill_climbing
from time import time

maze = {}
start = None
end = None
fileName = input("Digite o nome do arquivo: ")

with open(fileName, 'r') as fp:
    line = fp.readlines()
    height, width = [int(x) for x in line[0].split()]
    line = line[1:]
    for i, l in enumerate(line):
        for j, c in enumerate(l):
            if c == '\n':
                continue
            elif c == '#':
                start = (i, j)
            elif c == '$':
                end = (i, j)

            maze[(i, j)] = c 

maze['height'] = height
maze['width'] = width

########### Algoritmos ###########

t = time()
path = best_first_search(maze, start, end)
t2 = time()
print('\nBest_First_Search')
if path != None:
    print('Tempo de execução:' + str(t2-t))
    print('Posições percorridas: ')
    print(path, end='\n\n')
    print('Passos até o objetivo: {0}\n'.format(len(path)))
else:
    print('Nenhum caminho encontrado\n')

t = time()
try:
    path = depth_first_search(maze, start, end)
except Exception:
    path = None
t2 = time()
print('Depth_First_Search')
if path != None:
    print('Tempo de execução:' + str(t2-t))
    print('Posições percorridas: ')
    print(path, end='\n\n')
    print('Passos até o objetivo: {0}\n'.format(len(path)))
else:
    print('Nenhum caminho encontrado\n')

t1 = time()
path = breadth_first_search(maze, start, end)
t2 = time()
print('Breadth_First_Search')
if path != None:
    print('Tempo de execução:' + str(t2-t))
    print('Posições percorridas: ')
    print(path, end='\n\n')
    print('Passos até o objetivo: {0}\n'.format(len(path)))
else:
    print('Nenhum caminho encontrado\n')

t = time()    
path = astar_search(maze, start, end)
t2 = time()
print('Busca A*')
if path != None:
    print('Tempo de execução:' + str(t2-t))
    print('Posições percorridas: ')
    print(path, end='\n\n')
    print('Passos até o objetivo: {0}\n'.format(len(path)), end='\n\n')
else:
    print('Nenhum caminho encontrado\n')

t = time()
path = simple_hill_climbing(maze, start, end)
t2 = time()
print('Simple Hill Climbing')
if path != None:
    print('Tempo de execução:' + str(t2-t))
    print('Posições percorridas: ')
    print(path, end='\n\n')
    print('Passos até o objetivo: {0}'.format(len(path)), end='\n\n')
else:
    print('Nenhum caminho encontrado\n')
'''
Usage: python3 main.py

Input: name of file with the information of the maze, ex: input.txt

Output: Path found and number of steps for each of the algorithms
'''

from Search import best_first_search, depth_first_search, breadth_first_search, astar_search, simple_hill_climbing

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

path = best_first_search(maze, start, end)
print('\nBest_First_Search')
if path != None:
    print('Posições percorridas: ')
    print(path, end='\n\n')
    print('Passos até o objetivo: {0}\n'.format(len(path)))
else:
    print('Nenhum caminho encontrado')

path = depth_first_search(maze, start, end)
print('Depth_First_Search')
if path != None:
    print('Posições percorridas: ')
    print(path, end='\n\n')
    print('Passos até o objetivo: {0}\n'.format(len(path)))
else:
    print('Nenhum caminho encontrado')
    
path = breadth_first_search(maze, start, end)
print('Breadth_First_Search')
if path != None:
    print('Posições percorridas: ')
    print(path, end='\n\n')
    print('Passos até o objetivo: {0}\n'.format(len(path)))
else:
    print('Nenhum caminho encontrado')
    
path = astar_search(maze, start, end)
print('Busca A*')
if path != None:
    print('Posições percorridas: ')
    print(path, end='\n\n')
    print('Passos até o objetivo: {0}\n'.format(len(path)), end='\n\n')
else:
    print('Nenhum caminho encontrado')
    
path = simple_hill_climbing(maze, start, end)
print('Simple Hill Climbing')
if path != None:
    print('Posições percorridas: ')
    print(path, end='\n\n')
    print('Passos até o objetivo: {0}'.format(len(path)), end='\n\n')
else:
    print('Nenhum caminho encontrado')
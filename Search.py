from Block import Block, check_block

def best_first_search(maze, start_pos, end_pos, v=[]):   
    valids = [] # Can be visited
    closed = list(v) # Already visited

    start = Block(start_pos)
    goal = Block(end_pos)

    valids.append(start)
    
    while len(valids) > 0:
        valids.sort() # Find smaller cost

        current = valids.pop(0)
        closed.append(current)
        
        # Check if reached end of maze
        if current == goal:
            path = []
            while current != start:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Reverse to print in correct order

        (x, y) = current.position

        # Find neighbors
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for block in neighbors:
            # Get char from maze
            maze_value = maze.get(block)

            # If wall or invalid 
            if maze_value == None or maze_value == '-':
                continue

            neighbor = Block(block, current)

            # Check if was visited
            if(neighbor in closed):
                continue

            # Heuristic for cost (Manhattan distance)
            neighbor.distance_start = abs(neighbor.position[0] - start.position[0]) + abs(neighbor.position[1] - start.position[1])
            neighbor.distance_end = abs(neighbor.position[0] - goal.position[0]) + abs(neighbor.position[1] - goal.position[1])
            neighbor.distance_total = neighbor.distance_end

            # Check if already on open and if total distance is smaller
            if check_block(valids, neighbor):
                valids.append(neighbor)

    return None # No path found

def visit(maze, current, goal, visited):
    visited.append(current)
    
    x, y = current.position
    neighbors = []
    
    if x != 0:
        neighbors.append((x-1,y))
    if x < maze['height']-1:
        neighbors.append((x+1,y))
    if y != 0:
        neighbors.append((x,y-1))
    if y < maze['width']-1:
        neighbors.append((x,y+1))
    
    for block in neighbors:
        maze_value = maze.get(block)
        
        if maze_value == '-':
            continue
        
        neighbor = Block(block, current)
        
        if neighbor in visited:
            continue
            
        if neighbor == goal:
            return neighbor
        
        temp = visit(maze, neighbor, goal, visited)
        if temp is not None:
            return temp
    
    return None

def depth_first_search(maze, start_pos, end_pos):
    
    visited = []
    
    start = Block(start_pos)
    goal = Block(end_pos)
    
    goal = visit(maze, start, goal, visited)
    
    path = []
    while goal != start:
        path.append(goal.position)
        goal = goal.parent
    return path[::-1] # Reverse to print in correct order

def breadth_first_search(maze, start_pos, end_pos, v=[]):
    valids = []
    closed = list(v)
    neighbors = []

    start = Block(start_pos)
    goal = Block(end_pos)

    if start == goal:
        path = [start]
        return path
        
    valids.append(start)
    
    while len(valids) > 0:
        current = valids.pop(0)

        closed.append(current)
        
        (x, y) = current.position
        
        # Get neighbors
        if x > 0:
            neighbors.append((x-1,y))
        if x < maze['height']-1:
            neighbors.append((x+1,y))
        if y > 0:
            neighbors.append((x,y-1))
        if y < maze['width']-1:
            neighbors.append((x,y+1))

        for block in neighbors:
            maze_value = maze.get(block) # Get maze char

            # Check wall
            if(maze_value == '-'):
                continue

            neighbor = Block(block, current)

            # Check if visited
            if(neighbor in closed):
                continue
            
            if neighbor == goal:
                path = []
                while neighbor != start:
                    path.append(neighbor.position)
                    neighbor = neighbor.parent
                return path[::-1] # Reverse to print in correct order

            valids.append(neighbor)
        
        neighbors.clear()

    return None # No path found

def astar_search(maze, start_pos, end_pos):
    valids = []
    closed = []

    start = Block(start_pos)
    goal = Block(end_pos)

    valids.append(start)
    
    while len(valids) > 0:
        valids.sort() # Sort to find smallest

        current = valids.pop(0)
        closed.append(current)
        
        # Check if end is reached
        if current == goal:
            path = []
            while current != start:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Reverse to print in correct order

        (x, y) = current.position

        # Get neighbors
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for block in neighbors:
            maze_value = maze.get(block) # Get maze char 

            # Check if the node is a wall or invalid
            if maze_value == None or maze_value == '-':
                continue

            neighbor = Block(block, current)

            if neighbor in closed:
                continue

            # Get Manhattan distance
            neighbor.distance_start = abs(neighbor.position[0] - start.position[0]) + abs(neighbor.position[1] - start.position[1])
            neighbor.distance_end = abs(neighbor.position[0] - goal.position[0]) + abs(neighbor.position[1] - goal.position[1])
            neighbor.distance_total = neighbor.distance_start + neighbor.distance_end

            # Check if neighbor is in valid list and if it has a lower total cost
            if check_block(valids, neighbor):
                valids.append(neighbor)

    return None # No path found

def simple_hill_climbing(maze, start, end):
    current_path = best_first_search(maze, start, end) # Find initial solution

    if current_path != None: 
        # Optimize path found
        while 1:
            new_path = []
            # Test different paths
            for n in current_path[1:-1]:
                new_path = best_first_search(maze, start, end, v=[Block(n)])
                if new_path != None and len(new_path) < len(current_path):
                    current_path = new_path
                    break
            else:
                break

    return current_path
import random
from PIL import Image

class Maze:
    def __init__(self, size=100):
        self.visited = {}
        self.size = size

    def valid_movement(self, col, lin, move):
        if (
            (col + move[0]) < self.size * 2 - 1
            and (col + move[0]) >= 0
            and (lin + move[1]) < self.size * 2 - 1
            and (lin + move[1]) >= 0
        ):
            new_col = col + move[0]
            new_lin = lin + move[1]
            if (new_lin * self.size + new_col) not in self.visited:
                return True
        return False

    def find_neighbours(self, col, lin):
        moves = [[2, 0], [-2, 0], [0, 2], [0, -2]]
        neighbours = []
        for move in moves:
            if self.valid_movement(col, lin, move):
                neighbours.append((lin + move[1], col + move[0]))
        return neighbours

    def generate_maze(self):
        self.visited = {}
        X = random.randint(0, self.size - 1)
        Y = random.randint(0, self.size - 1)
        start_lin = lin = X if X % 2 == 0 else X - 1
        start_col = col = Y if Y % 2 == 0 else Y - 1
        self.visited[lin * self.size + col] = True

        maze = []
        for i in range(self.size * 2 - 1):
            aux = []
            for j in range(self.size * 2 - 1):
                aux.append("-")
            maze.append(aux)

        stack = []

        while len(self.visited) != self.size * self.size:
            maze[lin][col] = "*"
            neighbours = self.find_neighbours(lin=lin, col=col)
            if neighbours:
                if len(neighbours) > 1:
                    stack.append((lin, col))
                next_lin, next_col = random.choice(neighbours)

                maze[lin + round((next_lin - lin) / 2)][col + round((next_col - col) / 2)] = "*"

                lin = next_lin
                col = next_col
                self.visited[lin * self.size + col] = True
            else:
                next_lin = next_col = 0
                while len(stack):
                    next_lin, next_col = stack.pop()
                    if len(self.find_neighbours(lin=next_lin, col=next_col)):
                        break
                col = next_col
                lin = next_lin

        maze[lin][col] = "$"
        maze[start_lin][start_col] = "#"
        return maze

    def sava_maze(self, maze, filename="maze.txt"):
        with open(filename, "w") as f:
            for i in range(self.size * 2 - 1):
                for j in range(self.size * 2 - 1):
                    f.write(maze[i][j])
                f.write("\n")

    def visualize(self, maze, filename="maze.png"):
        imgx = 500
        imgy = 500
        image = Image.new("RGB", (imgx, imgy))
        pixels = image.load()
        color = {"*": (255, 255, 255), "-": (0, 0, 0), "#": (0, 255, 0), "$": (255, 0, 0)}

        # paint the maze
        for ky in range(imgy):
            for kx in range(imgx):
                x = color[maze[round(self.size * ky / imgy)][round(self.size * kx / imgx)]]
                pixels[kx, ky] = x
        image.save(filename, "PNG")
        image.show()


if __name__ == "__main__":
    maze_generator = Maze(10)
    maze = maze_generator.generate_maze()
    maze_generator.sava_maze(maze, filename=f"maze.txt")
    maze_generator.visualize(maze, filename=f"maze.png")
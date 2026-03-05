from cell import Cell


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = [[Cell(r, c) for c in range(cols)] for r in range(rows)]

    """ def print_maze (self):
        wall = "\033[48;2;254;254;254m  \033[0m"
        path = "\033[48;2;0;0;0m  \033[0m"
        print(wall * (self.cols * 2 + 1))
        for r in self.maze:
            line = wall
            bottom = wall
            for c in r:
                line += path
                if c.east:
                    line += wall
                else:
                    line += path
                if c.south:
                    bottom += wall
                else:
                    bottom += path
                bottom += wall
            print(line)
            print(bottom) """


    def print_maze(self):
        wall = "\033[48;2;254;254;254m  \033[0m"
        path = "\033[48;2;0;0;0m  \033[0m"
        for r in self.maze:
            line = ""
            top = ""
            for c in r:
                if c.west:
                    line += wall
                else:
                    line += path
                if c.north:
                    top += wall
                else:
                    top += path
                line += path
                top += wall
            top += wall
            line += wall
            print(top)
            print(line)
        print(wall * (self.cols * 2 + 1))


maze = Maze(10, 10)
maze.print_maze()

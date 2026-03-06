from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(r, c) for c in range(cols)] for r in range(rows)]

    def print_maze(self):
        print('\033[3J\033[H')
        wall = "\033[48;2;254;254;254m  \033[0m"
        path = "\033[48;2;0;0;0m  \033[0m"
        print(wall * (self.cols * 2 + 1))
        for r in self.grid:
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
            print(bottom)
        sleep(0.05)

    def has_unvisited_cells(self) -> bool:
        for r in self.grid:
            for c in r:
                if not c.visited:
                    return True
        return False

    def unvisited_neighbours(self, cell) -> list:
        unvisited = []
        if cell.row > 0 and not self.grid[cell.row - 1][cell.col].visited:
            unvisited.append(self.grid[cell.row - 1][cell.col])
        if cell.row < self.rows - 1 and not self.grid[cell.row + 1][cell.col].visited:
            unvisited.append(self.grid[cell.row + 1][cell.col])
        if cell.col < self.cols - 1 and not self.grid[cell.row][cell.col + 1].visited:
            unvisited.append(self.grid[cell.row][cell.col + 1])
        if cell.col > 0 and not self.grid[cell.row][cell.col - 1].visited:
            unvisited.append(self.grid[cell.row][cell.col - 1])
        return unvisited


    def backtracking(self, starting_cell=None):
        stack = []
        curr_cell = starting_cell
        curr_cell.visited = 1
        while self.has_unvisited_cells():
            unvisited = self.unvisited_neighbours(curr_cell)
            if unvisited:
                direction = random.choice(unvisited)
                curr_cell.break_wall(direction)
                direction.visited = 1
                if self.unvisited_neighbours(curr_cell):
                    stack.append(curr_cell)
                curr_cell = direction
            else:
                curr_cell = stack.pop()
            self.print_maze()

    def print_hexa_maze(self, filename=None):
        lines = []
        for r in self.grid:
            line = ""
            for c in r:
                line += format(c.hexa, "X")
            lines.append(line)
            if filename:
                with open(filename, "w") as f:
                    f.write("\n".join(lines))
            else:
                print(line)

m = Maze(10, 10)
m.backtracking(m.grid[0][0])
""" m.grid[0][0].break_wall(m.grid[0][1])
m.grid[0][0].break_wall(m.grid[1][0])
m.grid[0][5].break_wall(m.grid[0][6])
m.grid[4][0].break_wall(m.grid[5][0])
m.grid[0][5].break_wall(m.grid[1][5]) """
m.print_maze()
m.print_hexa_maze("hexa.txt")

from objects.cell import Cell
import pygame

class Board:
    def __init__(self, screen:pygame.Surface, width:int, height:int, cellSize:int):
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.screen = screen
        self.centerOffsetX = (screen.get_width() - self.width * self.cellSize) / 2
        self.centerOffsetY = (screen.get_height() - self.height * self.cellSize) / 2 + 10
        self.cells = [
            [Cell(
                self.screen,                
                pygame.Vector2(x, y),
                pygame.Vector2(
                    x * self.cellSize + self.centerOffsetX + 1,
                    y * self.cellSize + self.centerOffsetY + 1),
                self.cellSize
            )
            for x in range(width)]
            for y in range(height)
        ]
        
    def print_new_state(self, matrix):
        for row in matrix:
            for cell in row:
                print(cell, end="\t")
            print()
        print()
        
    def print_cells(self, cells):
        for row in cells:
            for cell in row:
                print(cell.isAlive, end="\t")
            print()
        print()

    def update(self, dt):
        next_state = [[False for _ in range(self.width)] for _ in range(self.height)]
        
        # Calculate the next state
        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                aliveCount = self.getNeighbors(cell)
                if cell.isAlive:
                    if aliveCount < 2 or aliveCount > 3:
                        next_state[y][x] = False
                    else:
                        next_state[y][x] = True
                else:
                    if aliveCount == 3:
                        next_state[y][x] = True

        # Apply the next state
        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                cell.isAlive = next_state[y][x]

    def getNeighbors(self, cell: Cell):
        aliveNeighborsCount = 0
        for y in range(-1, 2):
            for x in range(-1, 2):
                # Skip the cell itself
                if x == 0 and y == 0:
                    continue

                # Calculate neighbor's grid position
                neighbor_x = int(cell.pos.x + x)
                neighbor_y = int(cell.pos.y + y)

                # Check if the neighbor is within grid bounds
                if 0 <= neighbor_x < self.width and 0 <= neighbor_y < self.height:
                    if self.cells[neighbor_y][neighbor_x].isAlive:
                        aliveNeighborsCount += 1
        return aliveNeighborsCount

    def clear(self):
        self.cells = [
            [Cell(
                self.screen,                
                pygame.Vector2(x, y),
                pygame.Vector2(
                    x * self.cellSize + self.centerOffsetX + 1,
                    y * self.cellSize + self.centerOffsetY + 1),
                self.cellSize
            )
            for x in range(self.width)]
            for y in range(self.height)
        ]

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0 + self.centerOffsetX, 0 + self.centerOffsetY, self.width * self.cellSize + 2, self.height * self.cellSize + 2), 1)
        for row in self.cells:
            for cell in row:
                cell.draw()
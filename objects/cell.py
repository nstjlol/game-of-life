import pygame

class Cell:
    def __init__(self, screen:pygame.Surface, pos:pygame.Vector2, size=10, alive:bool = False):
        self.isAlive = alive
        self.size = size
        self.aliveColor = "white"
        self.deadColor = "black"
        self.screen = screen
        self.pos = pos

    def is_over(self, mouse_pos:tuple):
        if mouse_pos[0] > self.pos.x and mouse_pos[0] < self.pos.x + self.size:
            if mouse_pos[1] > self.pos.y and mouse_pos[1] < self.pos.y + self.size:
                return True
        return False

    def draw(self):
        pygame.draw.rect(self.screen, (20,20,20), pygame.Rect(self.pos.x, self.pos.y, self.size, self.size), 1)
        drawColor = self.deadColor
        if self.isAlive:
            drawColor = self.aliveColor
        pygame.draw.rect(self.screen, drawColor, pygame.Rect(self.pos.x+1, self.pos.y+1, self.size-2, self.size-2))

    def spawn(self):
        self.isAlive = True
        self.color = "white"
    
    def kill(self):
        self.isAlive = False
        self.color = "black"

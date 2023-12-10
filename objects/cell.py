import pygame

class Cell:
    def __init__(self, screen:pygame.Surface, pos:pygame.Vector2, screen_pos:pygame.Vector2, size=10, alive:bool = False):
        self.isAlive = alive
        self.size = size
        self.aliveColor = "white"
        self.deadColor = "black"
        self.screen = screen
        self.pos = pos
        self.screen_pos = screen_pos

    def is_over(self, mouse_pos:tuple):
        if mouse_pos[0] > self.screen_pos.x and mouse_pos[0] < self.screen_pos.x + self.size:
            if mouse_pos[1] > self.screen_pos.y and mouse_pos[1] < self.screen_pos.y + self.size:
                return True
        return False

    def draw(self):
        pygame.draw.rect(self.screen, (20,20,20), pygame.Rect(self.screen_pos.x, self.screen_pos.y, self.size, self.size), 1)
        drawColor = self.deadColor
        if self.isAlive:
            drawColor = self.aliveColor
        pygame.draw.rect(self.screen, drawColor, pygame.Rect(self.screen_pos.x+1, self.screen_pos.y+1, self.size-2, self.size-2))

    def spawn(self):
        self.isAlive = True
        self.color = "white"
    
    def kill(self):
        self.isAlive = False
        self.color = "black"

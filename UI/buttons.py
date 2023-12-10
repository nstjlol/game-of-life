import pygame

class ToggleButton:
    def __init__(self, pos:pygame.Vector2, size:pygame.Vector2, color:pygame.Color = (30,30,30), background_color:pygame.Color = (220,220,220), text:str = "", clicked:bool = False):
        self.pos = pos
        self.size = size
        self.origColor = color
        self.origBackgroundColor = background_color
        if clicked:
            self.color = background_color
            self.backgroundColor = color
        else:
            self.color = color
            self.backgroundColor = background_color
        self.text = text

        self.clicked = clicked

    def draw(self, screen:pygame.Surface):
        pygame.draw.rect(screen, self.backgroundColor, pygame.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y), border_radius=5)

        if self.text != "":
            font = pygame.font.SysFont('Arial', 25)
            text_surface = font.render(self.text, True, self.color)

            # Calculate text surface size
            text_size = text_surface.get_size()

            # Calculate the x and y position to center the text
            text_x = self.pos.x + (self.size.x - text_size[0]) / 2
            text_y = self.pos.y + (self.size.y - text_size[1]) / 2

            screen.blit(text_surface, (text_x, text_y))

    def is_over(self, mouse_pos:tuple):
        if mouse_pos[0] > self.pos.x and mouse_pos[0] < self.pos.x + self.size.x:
            if mouse_pos[1] > self.pos.y and mouse_pos[1] < self.pos.y + self.size.y:
                return True
        return False
    
    def click(self, state:bool = None):
        if state != None:
            self.clicked = not self.clicked
            if self.clicked:
                self.color, self.backgroundColor = self.origBackgroundColor, self.origColor
            else:
                self.color, self.backgroundColor = self.origColor, self.origBackgroundColor
        else:
            self.clicked = state
            if self.clicked:
                self.color, self.backgroundColor = self.origBackgroundColor, self.origColor
            else:
                self.color, self.backgroundColor = self.origColor, self.origBackgroundColor

        if self.clicked:
            self.onClick()

    def onClick(self):
        pass
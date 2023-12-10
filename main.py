import pygame
from UI.strings import DictKeys, game_info, ui_string
from UI.buttons import ToggleButton
from objects.board import Board

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption(game_info[DictKeys.TITLE])
running = True
playing = False
dt = 0

mouse_pos = pygame.Vector2(0, 0)

spawnTool = ToggleButton(pygame.Vector2(10, 10), pygame.Vector2(100, 50), color=(30,30,90), text=ui_string[DictKeys.ADD], clicked=True)
killTool = ToggleButton(pygame.Vector2(120, 10), pygame.Vector2(100, 50), color=(30,30,90), text=ui_string[DictKeys.REMOVE], clicked=False)
tools = [spawnTool, killTool]
selectedTool = 0

board = Board(screen, 20, 10, 40)

while running:
    # poll for events
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = not playing
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, tool in enumerate(tools):
                if tool.is_over(mouse_pos) and not tool.clicked:
                    selectedTool = i
                    tool.click(True)
                    for j, otherTool in enumerate(tools):
                        if j != i:
                            otherTool.click(False)
                    break
            for row in board.cells:
                for cell in row:
                    if cell.is_over(mouse_pos):
                        if selectedTool == 0:
                            cell.spawn()
                        elif selectedTool == 1:
                            cell.kill()
    
    if playing:
        board.update(dt)

    # Wipe the screen clean and draw...
    screen.fill((30,30,30))
    # ...tools
    spawnTool.draw(screen)
    killTool.draw(screen)
    #...grid
    board.draw()

    # flip() the display to put your changes on the screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # Limits the game to 60 fps

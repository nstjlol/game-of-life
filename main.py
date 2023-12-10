import pygame
from time import sleep
from UI.strings import DictKeys, game_info, ui_string
from UI.buttons import ToggleButton
from objects.board import Board

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption(game_info[DictKeys.TITLE])
running = True
playing = False
play_once = False
dt = 0

mouse_pos = pygame.Vector2(0, 0)

spawnTool = ToggleButton(pygame.Vector2(10, 10), pygame.Vector2(100, 50), color=(30,30,90), text=ui_string[DictKeys.ADD], clicked=True)
killTool = ToggleButton(pygame.Vector2(120, 10), pygame.Vector2(100, 50), color=(30,30,90), text=ui_string[DictKeys.REMOVE], clicked=False)
clearTool = ToggleButton(pygame.Vector2(230, 10), pygame.Vector2(100, 50), color=(30,30,90), text="Clear", clicked=False)
tools = [spawnTool, killTool]
selectedTool = 0
delayTime = 100

board = Board(screen, 80, 40, 15)

while running:
    # poll for events
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = not playing
            if event.key == pygame.K_RETURN:
                play_once = True
            if event.key == pygame.K_r:
                board.print_cells(board.cells)
            if event.key == pygame.K_UP:
                delayTime -= 100
            if event.key == pygame.K_DOWN:
                delayTime += 100
                
        overCell = False
        overTool = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                for row in board.cells:
                    for cell in row:
                        if cell.is_over(mouse_pos):
                            if selectedTool == 0:
                                cell.spawn()
                            elif selectedTool == 1:
                                cell.kill()
                            overCell = True
                                
                # Check if the mouse is over a tool
                if not overCell:
                    if clearTool.is_over(mouse_pos):
                        board.clear()
                    
                    for i, tool in enumerate(tools):
                        if tool.is_over(mouse_pos) and i != selectedTool:
                            selectedTool = i
                            tool.click(True)
                            overTool = True
                    if overTool:
                        for tool in tools:
                            if tool != tools[selectedTool]:
                                tool.click(False)

    # Wipe the screen clean and draw...
    screen.fill((30,30,30))
    # ...tools
    spawnTool.draw(screen)
    killTool.draw(screen)
    clearTool.draw(screen)
    #...grid    
    if playing or play_once:
        play_once = False
        board.update(dt)
        board.draw()
        pygame.time.delay(delayTime)
    else:
        board.draw()

    # flip() the display to put your changes on the screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # Limits the game to 60 fps
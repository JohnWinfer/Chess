import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP

pygame.init()

clock = pygame.time.Clock()

white = (27, 20, 16)
tileColour1 = (125, 77, 52)
tileColour2 = (201, 186, 149)

size = (1200, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess")

programRunning = True



def drawGrid():
    tilecount = 0
    global xcord, ycord
    count = 0
    for i in range(0, 8):
        for i in range (0, 8):
            if count % 2 == 0:
                pygame.draw.rect(screen, tileColour1, [xcord, ycord, 100, 100], 0)
            else:
                pygame.draw.rect(screen, tileColour2, [xcord, ycord, 100, 100], 0)
            count = count + 1
            tilecount = tilecount + 1
            xcord = xcord + 100
        count = count + 1
        xcord = 200
        ycord = ycord + 100

while programRunning:
    for event in pygame.event.get():
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            programRunning = False
    screen.fill(white)

    xcord = 200
    ycord = 0
    drawGrid()

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
quit()

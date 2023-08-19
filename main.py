import time
import pygame
pygame.init()
spikes=[(1000, 0)]
screen = pygame.display.set_mode((1300, 700))
pygame.display.set_caption('Geometry Dash')
clock = pygame.time.Clock()
jump = False
jumpBuffer = False
mainloop = True
camPosX = 0
camPosY = 0
cubePosX = 200
cubePosY = 500
gr1x = 0
notjump = True
move = True
jumpstep = 0
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            jump = True
            jumpBuffer = True
        elif event.type == pygame.KEYUP:
            jump = False
            jumpBuffer = False
    screen.fill((10,10,255))
    if jump:
        if notjump:
            notjump = False
    if notjump == False:
        if jumpstep < 19:
            jumpstep = jumpstep + 1
            cubePosY = cubePosY - 7
        if jumpstep > 18:
            jumpstep = jumpstep + 1
            cubePosY = cubePosY + 7
        if jumpstep > 37:
            notjump = True
            jumpstep = 0
    if move:
        camPosX = camPosX + 7
        cubePosX = cubePosX + 7
        gr1x = gr1x + 7
    for spike in spikes:
        spikeX,spikeY = spike
        pygame.draw.rect(screen, (0,0,0), (spikeX-camPosX, spikeY+500-camPosY, 50,50))
    pygame.draw.rect(screen, (250,200,0), (cubePosX-camPosX, cubePosY-camPosY, 50,50))
    pygame.draw.rect(screen, (50, 50, 255), (gr1x-camPosX, 551-camPosY, 1300, 700))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

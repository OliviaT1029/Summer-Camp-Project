import pygame #import module
pygame.init() #initalize pygame module
screen = pygame.display.set_mode((1000,700)) #draw window
pygame.display.set_caption("Olivia's Game")
clock = pygame.time.Clock()
screen.fill((203,255,203))

close = False
while not close: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
    
    pygame.display.update() #refresh screen
    clock.tick(60) #frame rate
pygame.quit()
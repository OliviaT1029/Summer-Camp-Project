import pygame #import module
pygame.init() #initalize pygame module
screensize = (1000,700)
screen = pygame.display.set_mode(screensize) #draw window
pygame.display.set_caption("Olivia's Game")
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
blue = (203,255,203)
clock = pygame.time.Clock()
paddlesize = [100,40]
paddlex = screensize[0]/2

screen.fill((203,255,203))

close = False
while not close: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            paddlex=paddlex+10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                paddlex=paddlex-10          
    
    screen.fill(blue)
    pygame.draw.rect(screen,black,(paddlex,600,paddlesize[0],paddlesize[1]))
    pygame.display.update() #refresh screen
    clock.tick(60) #frame rate
pygame.quit()
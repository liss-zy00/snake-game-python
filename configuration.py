import pygame

class Config():
    global screen 
    
    def screenDefinition():
        global screen 

        screenWidth = 720
        screenHeight = 480
        screen = pygame.display.set_mode((screenWidth, screenHeight))
    
    def gameLoop():
        Config.screenDefinition()
        
        snakeSpeed = 30
        clock = pygame.time.Clock()
        running = True

        while running:
            screen.fill((0,0,0))

            pygame.display.flip()
            clock.tick(snakeSpeed)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

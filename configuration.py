import pygame

class Config():
    
    def screenDefinition():
        global screen, screenWidth, screenHeight

        screenWidth = 720
        screenHeight = 480
        screen = pygame.display.set_mode((screenWidth, screenHeight))

    def gameLoop():
        global event

        Config.screenDefinition()
        Config.snakeSpawn()
        Config.speedSetting()
        
        clock = pygame.time.Clock()
        running = True

        while running:
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 255, 0), [snakeX, snakeY, 10, 10]) #snake square
            
            Config.snakePositionUpdate()

            pygame.display.flip()
            clock.tick(snakeSpeed)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Config.keyboardEventListener()

                if event.type == pygame.QUIT:
                    running = False

    def snakeSpawn():
        global snakeSpeed, snakeX, snakeY
        
        snakeX = screenWidth / 2
        snakeY = screenHeight / 2
        snakeSpeed = 50

        #snakSize = 10
        #snakeLength = 1
        #snakeBlocks = []

    def speedSetting():
        global speedX, speedY

        speedX = 0
        speedY = 0

    def snakePositionUpdate():
        global snakeX, snakeY

        snakeX += speedX
        snakeY += speedY
    
    def keyboardEventListener():
        global speedX, speedY

        if event.key == pygame.K_UP:
            speedX = 0
            speedY = -2
            
        if event.key == pygame.K_DOWN:
            speedX = 0
            speedY = 2

        if event.key == pygame.K_LEFT:
            speedY = 0
            speedX = -2
            
        if event.key == pygame.K_RIGHT:
            speedY = 0
            speedX = 2


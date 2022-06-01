import pygame
import random

class Config():
    
    def screenDefinition():
        global screen, screenWidth, screenHeight

        screenWidth = 720
        screenHeight = 480
        screen = pygame.display.set_mode((screenWidth, screenHeight))

    def gameLoop():
        global event, gameOver
        pygame.init()

        Config.colors()
        Config.screenDefinition()
        Config.snakeSpawn()
        Config.fruitPositionSetting()
        Config.snakeSpeedSetting()
        
        clock = pygame.time.Clock()
        running = True
        gameOver = False

        while running:
            if not gameOver:
                screen.fill(black)

                pygame.draw.rect(screen, green, [snakeX, snakeY, 10, 10]) #snake square
                Config.snakeSizeUpdate()
            
                pygame.draw.rect(screen, red, [fruitX, fruitY, 10, 10]) #fruit square
                
                Config.snakePositionUpdate()
                Config.fruitRandomSpawn()
                Config.snakeWallCollision()

            else:
                screen.fill(white)
                Config.message_display(f"Final Score: {gameScore}", screenWidth / 2, 100, 25, black)
                
            Config.message_display(f"Score: {gameScore}", 60, 25, 25, white)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(snakeSpeed)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Config.keyboardEventListener()

                if event.type == pygame.QUIT:
                    running = False
    
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
    
    def text_objects(text, font, color):
        global textSurface

        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def message_display(text, textLargura, textAltura, size, color):
        global theFont

        theFont = pygame.font.Font("freesansbold.ttf", size)
        textSurf, textRect = Config.text_objects(text, theFont, color)
        textRect.center =(textLargura, textAltura)
        screen.blit(textSurf, textRect)

    def colors():
        global black, white, green, red

        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (0, 255, 0)
        red = (255, 0, 0)

#snake settings
    def snakeSpawn():
        global snakeX, snakeY, snakeSpeed, snakeSize, snakeLength, snakeBlocks, gameScore

        snakeX = screenWidth / 2
        snakeY = screenHeight / 2
        snakeSpeed = 40

        snakeSize = 10
        snakeLength = 1
        snakeBlocks = []

        gameScore = 0

    def snakeSpeedSetting():
        global speedX, speedY

        speedX = 0
        speedY = 0

    def snakePositionUpdate():
        global snakeX, snakeY

        snakeX += speedX
        snakeY += speedY

    def snakeSizeUpdate():
        global snakeHead, snakeBlocks

        snakeHead = []
        snakeHead.append(snakeX)
        snakeHead.append(snakeY)
        snakeBlocks.append(snakeHead)

        if len(snakeBlocks) > snakeLength:
            del snakeBlocks[0]
        
        Config.snakeTailCollision()

        for block in snakeBlocks:
            pygame.draw.rect(screen, green, [block[0], block[1], snakeSize, snakeSize])

    def snakeWallCollision():
        global gameOver

        if (snakeX >= screenWidth or snakeX < 0 or snakeY >= screenHeight or snakeY < 0):
            gameOver = True

    def snakeTailCollision():
        global gameOver

        for x in snakeBlocks[:-1]:
            if x == snakeHead:
                gameOver = True

#fruit settings
    def fruitPositionSetting():
        global fruitX, fruitY

        fruitX = 300
        fruitY = 400

    def fruitRandomSpawn():
        global fruitX, fruitY, snakeLength, gameScore

        if snakeX == fruitX and snakeY == fruitY:
            gameScore += 1
            snakeLength += 5 #????? 
            fruitX = round(random.randrange(0, screenWidth - 10) / 10.0) * 10.0
            fruitY = round(random.randrange(0, screenHeight - 10) / 10.0) * 10.0

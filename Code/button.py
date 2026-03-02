import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

button_img = pygame.image.load("button.png").convert()
button2_img = pygame.image.load("button2.png").convert()
font = pygame.font.Font(None, size=40)
running = True
counter = 0
clock = pygame.time.Clock()
while running:
    
    screen.blit(button_img, (0, 0))
    text = font.render(str(counter), True, (0, 0, 0))
    screen.blit(text,(300, 300))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                counter += 1
                screen.blit(button2_img, (0, 0))
                pygame.display.flip()
                pygame.time.delay(50)
                screen.blit(button_img, (0, 0))
                pygame.display.flip()
                
    if counter == 0:
        text2 = font.render(("Press SPACE"), True, (0, 0, 0))
        screen.blit(text2, (230, 20))
    
    if event.type == pygame.QUIT:
        running = False
            
            
            
    pygame.display.flip()

    clock.tick(60)
    
pygame.quit()
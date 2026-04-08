import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Flip image")
img1 = pygame.image.load("SteveProXNA.jpg")
img2 = img1
img3 = img1
img2 = pygame.transform.flip(img2, True, False)
img3 = pygame.transform.flip(img3, False, True)
done = False

bg = (127, 127, 127)

while not done:
    for event in pygame.event.get():
        screen.fill(bg)
        rect1 = img1.get_rect()
        rect1.center = 200, 50
        screen.blit(img1, rect1)
        rect2 = img2.get_rect()
        rect2.center = 200, 150
        screen.blit(img2, rect2)
        rect3 = img3.get_rect()
        rect3.center = 200, 250
        screen.blit(img3, rect3)

        if event.type == pygame.QUIT:
            done = True

    pygame.display.update()

pygame.quit()
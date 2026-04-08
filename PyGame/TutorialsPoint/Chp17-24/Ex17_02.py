import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Rotate image")
img1 = pygame.image.load("SteveProXNA.jpg")
img2 = img1
img3 = img1
img2 = pygame.transform.rotate(img2, 90)
img3 = pygame.transform.rotate(img3, -90)
done = False

bg = (127, 127, 127)

while not done:
    for event in pygame.event.get():
        screen.fill(bg)
        rect1 = img1.get_rect()
        rect1.center = 200, 50
        screen.blit(img1, rect1)
        rect2 = img2.get_rect()
        rect2.center = 100, 200
        screen.blit(img2, rect2)
        rect3 = img3.get_rect()
        rect3.center = 300, 200
        screen.blit(img3, rect3)

        if event.type == pygame.QUIT:
            done = True

    pygame.display.update()

pygame.quit()
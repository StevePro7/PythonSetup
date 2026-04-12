import pygame
import pygame.camera

pygame.init()
gameDisplay = pygame.display.set_mode((640,480))
pygame.camera.init()
print(pygame.camera.list_cameras())
cam = pygame.camera.Camera(0)
cam.start()

playing = True
while playing:
    imghdr = cam.get_image()
    gameDisplay.blit(imghdr,(0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cam.stop()
            playing = False
            pygame.quit()
            exit()

pygame.quit()
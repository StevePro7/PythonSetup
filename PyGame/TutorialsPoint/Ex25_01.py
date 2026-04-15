import pygame
import random


class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()


pygame.init()
clock = pygame.time.Clock()

screen_width = 640
screen_height = 480

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20,15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)


# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)

screen = pygame.display.set_mode((screen_width, screen_height))

score: int = 0
done: bool = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(WHITE)

    # Get the current mouse position
    # this returns the position as a list of two numbers
    pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list
    # just like we'd fetch letters out of a string

    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # See if the player block has collided with anything
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # Check the list of collisions
    for block in blocks_hit_list:
        score += 1
        print(score)

    # Draw all the sprites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

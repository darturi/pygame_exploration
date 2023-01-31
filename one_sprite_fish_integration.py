import fish
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("one_sprite")

WHITE = (255, 255, 255)
FPS = 60


def draw_window(sprite):
    WIN.fill(WHITE)
    WIN.blit(sprite.sprite, (sprite.sprite_loc.x, sprite.sprite_loc.y))

    sprite.update_loc()

    pygame.display.update()


def main():
    sprite = fish.Fish()
    sprite.rotate_sprite(90)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(sprite)

    pygame.quit()


main()
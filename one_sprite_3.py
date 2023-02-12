import fish2
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
    # print(sprite.in_turn)

    pygame.display.update()


def main():
    sprite = fish2.Fish()
    sprite.rotate_sprite(-90)
    print(sprite.sprite_loc.x, sprite.sprite_loc.y)
    print(sprite.define_tip())
    input()
    sprite.rotate_sprite(45)
    print(sprite.sprite_loc.x, sprite.sprite_loc.y)
    print(sprite.define_tip())

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        """keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            sprite.rotate_sprite(10, False)
        elif keys_pressed[pygame.K_RIGHT]:
            sprite.rotate_sprite(10)"""

        draw_window(sprite)

        # input()


    pygame.quit()


if __name__ == "__main__":
    main()
from archived import fish2
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("one_sprite")

WHITE = (0, 255, 255)
FPS = 60


def draw_window(sprite):
    WIN.fill(WHITE)
    # WIN.blit(sprite.sprite, (sprite.sprite_loc.x, sprite.sprite_loc.y))

    sprite.update_loc()
    # print(sprite.in_turn)

    pygame.display.update()


def main():
    sprite = fish2.Fish(WIN)
    # sprite.find_turn_axis(0)
    print(sprite.sprite_loc.x, sprite.sprite_loc.y)

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

        input()
        print(sprite.sprite_loc.x, sprite.sprite_loc.y)

        draw_window(sprite)

        # input()


    pygame.quit()


if __name__ == "__main__":
    main()
import fish3
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
    sprite = fish3.Fish(WIN)
    # sprite.find_turn_axis(0)
    sprite.get_future_center()
    sprite.rotate_sprite(45)
    sprite.get_future_center()
    print(sprite.sprite_loc.x, sprite.sprite_loc.y)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # input()
        # print(sprite.sprite_loc.x, sprite.sprite_loc.y)
        draw_window(sprite)

        # input()


    pygame.quit()


if __name__ == "__main__":
    main()
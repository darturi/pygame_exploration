import fish5
import pygame
import music_quantifier_1

WIDTH, HEIGHT = 900, 500
SPRITE_W, SPRITE_H = 40, 40
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("one_sprite")

WHITE = (0, 255, 255)
FPS = 60

audio_path = "assets/violin.wav"


def draw_window(sprite):
    WIN.fill(WHITE)
    sprite.update_loc()
    pygame.display.update()


def main():
    # Initialize path info
    pos_path, neg_path = music_quantifier_1.get_scaled_pos_neg(audio_path, WIDTH, SPRITE_W)

    sprite = fish5.Fish(WIN, pos_path)
    sprite.get_future_center()
    #sprite.rotate_sprite(45)
    sprite.get_future_center()
    print(sprite.sprite_loc.x, sprite.sprite_loc.y)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # print(sprite.sprite_loc.x, sprite.sprite_loc.y)
        draw_window(sprite)

        # input()


    pygame.quit()


if __name__ == "__main__":
    main()
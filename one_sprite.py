import os.path

import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("one_sprite")

WHITE = (255, 255, 255)

FPS = 60
VEL = 5
SPRITE_W, SPRITE_H = 40, 40


def create_arrow_sprite(w=SPRITE_W, h=SPRITE_H):
    arrow_sprite = pygame.image.load(os.path.join('assets', 'arrow.png'))
    return pygame.transform.scale(arrow_sprite, (w, h))


def rotate_sprite(sprite_name, angle, right=True):
    if not right:
        angle *= -1

    return pygame.transform.rotate(sprite_name, angle)


def draw_window(arrow_loc):
    WIN.fill(WHITE)
    WIN.blit(arrow, (arrow_loc.x, arrow_loc.y))
    pygame.display.update()


def update_loc(arrow_loc, velocity=VEL):
    arrow_loc.x += velocity
    arrow_loc.y += velocity


def main():
    arrow_loc = pygame.Rect(400, 200, SPRITE_W, SPRITE_H)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update_loc(arrow_loc)

        draw_window(arrow_loc)

    pygame.quit()


arrow = create_arrow_sprite()
arrow = rotate_sprite(arrow, 90, False)

main()
import os.path

import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("one_sprite")

WHITE = (255, 255, 255)

OUTER_PADDING, INNER_PADDING_THICKNESS = 50, 5

FPS = 60
VEL = 5
SPRITE_W, SPRITE_H = 40, 40
START_X, START_Y = 400, 200


def create_arrow_sprite(w=SPRITE_W, h=SPRITE_H):
    arrow_sprite = pygame.image.load(os.path.join('assets', 'arrow.png'))
    return pygame.transform.scale(arrow_sprite, (w, h))


def rotate_sprite(sprite_name, angle, right=True):
    if not right:
        angle *= -1
    return pygame.transform.rotate(sprite_name, angle)


def determine_velocity(arrow_loc, prev_x_velocity=VEL, prev_y_velocity=VEL):
    new_x, new_y = prev_x_velocity, prev_y_velocity
    if not in_outer_padding(arrow_loc) and in_inner_padding(arrow_loc):
        if arrow_loc.x <= OUTER_PADDING + INNER_PADDING_THICKNESS or \
                arrow_loc.x >= WIDTH - (OUTER_PADDING + INNER_PADDING_THICKNESS):
            new_x *= -1
        if arrow_loc.y <= OUTER_PADDING + INNER_PADDING_THICKNESS or \
                arrow_loc.y >= HEIGHT - (OUTER_PADDING + INNER_PADDING_THICKNESS):
            new_y *= -1
    return new_x, new_y


def draw_window(arrow_loc, x_vel, y_vel):
    WIN.fill(WHITE)
    WIN.blit(arrow, (arrow_loc.x, arrow_loc.y))

    update_loc(arrow_loc, x_vel, y_vel)

    pygame.display.update()


def in_outer_padding(arrow_loc, padding=OUTER_PADDING):
    # Add functionality that takes into account the dimensions of the sprite
    # HERE
    # check if in outer padding
    if arrow_loc.x <= padding or arrow_loc.x >= WIDTH - padding or \
            arrow_loc.y <= padding or arrow_loc.y >= HEIGHT - padding:
        return True
    return False


def in_inner_padding(arrow_loc, padding=OUTER_PADDING, thickness=INNER_PADDING_THICKNESS):
    return not in_outer_padding(arrow_loc) and in_outer_padding(arrow_loc, padding + thickness)


def update_loc(arrow_loc, x_vel=VEL, y_vel=VEL):
    arrow_loc.x += x_vel
    arrow_loc.y += y_vel


def main():
    # define arrow start position
    arrow_loc = pygame.Rect(START_X, START_Y, SPRITE_W, SPRITE_H)
    x_vel, y_vel = VEL, VEL
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        x_vel, y_vel = determine_velocity(arrow_loc, x_vel, y_vel)
        draw_window(arrow_loc, x_vel, y_vel)

    pygame.quit()


arrow = create_arrow_sprite()
arrow = rotate_sprite(arrow, 90, False)

main()
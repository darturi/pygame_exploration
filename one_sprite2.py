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


def determine_velocity(arrow_loc, prev_x_velocity, prev_y_velocity, padding=50):
    print("in_outer_padding(arrow_loc)", in_outer_padding(arrow_loc), "   in_inner_padding(arrow_loc)", in_inner_padding(arrow_loc))
    new_x, new_y = prev_x_velocity, prev_y_velocity
    # if not in_outer_padding(arrow_loc) and in_inner_padding():
    #     if
    return new_x, new_y


def draw_window(arrow_loc):
    WIN.fill(WHITE)
    WIN.blit(arrow, (arrow_loc.x, arrow_loc.y))

    """if not arrow_prev_state and not in_outer_padding(arrow_loc):
        update_loc(arrow_loc, arrow_prev_state, -1, -1)
    else:
        update_loc(arrow_loc, arrow_prev_state)"""
    update_loc(arrow_loc)

    pygame.display.update()


def in_outer_padding(arrow_loc, padding=OUTER_PADDING):
    # check if in outer padding
    if arrow_loc.x <= padding or arrow_loc.x >= WIDTH - padding or \
            arrow_loc.y <= padding or arrow_loc.y >= HEIGHT - padding:
        return True
    return False


def in_inner_padding(arrow_loc, padding=OUTER_PADDING, thickness=INNER_PADDING_THICKNESS):
    return not in_outer_padding(arrow_loc) and in_outer_padding(arrow_loc, padding + thickness)


def update_loc(arrow_loc, x_vel=VEL, y_vel=VEL):
    """# check if x flipping is needed
    if arrow_loc.x == threshold or arrow_loc.x == WIDTH - threshold:
        x_velocity *= -1
    # check if y flipping is needed
    if arrow_loc.y == threshold or arrow_loc.y == HEIGHT - threshold:
        y_velocity *= -1"""

    x_vel, y_vel = determine_velocity(arrow_loc, x_vel, y_vel)

    arrow_loc.x += x_vel
    arrow_loc.y += y_vel


def main():
    # define arrow start position
    arrow_loc = pygame.Rect(START_X, START_Y, SPRITE_W, SPRITE_H)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(arrow_loc)

        input()

    pygame.quit()


arrow = create_arrow_sprite()
arrow = rotate_sprite(arrow, 90, False)

main()
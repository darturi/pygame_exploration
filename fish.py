import pygame
import os


class Fish:
    VEL = 5
    OUTER_PADDING, INNER_PADDING_THICKNESS = 50, 5
    CANVAS_WIDTH, CANVAS_HEIGHT = 900, 500
    START_X, START_Y = 400, 200
    SPRITE_H, SPRITE_W = 40, 40

    def __init__(self, sprite_w=SPRITE_W, sprite_h=SPRITE_H, start_x=START_X, start_y=START_Y, start_vel=VEL):
        arrow_sprite = pygame.image.load(os.path.join('assets', 'arrow.png'))

        self.sprite = pygame.transform.scale(arrow_sprite, (sprite_w, sprite_h))
        self.angle = 0
        self.sprite_loc = pygame.Rect(start_x, start_y, sprite_w, sprite_h)
        self.prev_x_vel = start_vel
        self.prev_y_vel = start_vel

    def rotate_sprite(self, angle, right=True):
        if not right:
            angle *= -1
        self.angle += angle
        self.sprite = pygame.transform.rotate(self.sprite, angle)

    def update_loc(self): #, x_vel=VEL, y_vel=VEL):
        x_vel, y_vel = self.determine_velocity()
        self.sprite_loc.x += x_vel
        self.sprite_loc.y += y_vel

    def in_outer_padding(self, padding=OUTER_PADDING, canvas_w=CANVAS_WIDTH, canvas_h=CANVAS_HEIGHT):
        return self.sprite_loc.x <= padding or self.sprite_loc.x >= canvas_w - padding \
               or self.sprite_loc.y <= padding or self.sprite_loc.y >= canvas_h - padding

    def in_inner_padding(self, padding=OUTER_PADDING, thickness=INNER_PADDING_THICKNESS):
        return not self.in_outer_padding() and self.in_outer_padding(padding=padding + thickness)

    def determine_velocity(self, padding=OUTER_PADDING,
                           thickness=INNER_PADDING_THICKNESS, canvas_w=CANVAS_WIDTH, canvas_h=CANVAS_HEIGHT):
        if not self.in_outer_padding() and self.in_inner_padding():
            if self.sprite_loc.x <= padding + thickness or \
                    self.sprite_loc.x >= canvas_w - (padding + thickness):
                self.prev_x_vel *= -1
            if self.sprite_loc.y <= padding + thickness or \
                    self.sprite_loc.y >= canvas_h - (padding + thickness):
                self.prev_y_vel *= -1
        return self.prev_x_vel, self.prev_y_vel


sprite = Fish()
print(type(sprite.sprite_loc.x))

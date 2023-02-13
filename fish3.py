import math
import pygame
import os


class Fish:
    VEL = 2
    OUTER_PADDING, INNER_PADDING_THICKNESS = 50, 2
    CANVAS_WIDTH, CANVAS_HEIGHT = 900, 500
    START_X, START_Y = 400, 200
    SPRITE_H, SPRITE_W = 40, 40

    def __init__(self, window, sprite_w=SPRITE_W, sprite_h=SPRITE_H, start_x=START_X, start_y=START_Y):
        arrow_sprite = pygame.image.load(os.path.join('assets', 'arrow.png')).convert()

        self.win = window
        self.sprite = pygame.transform.scale(arrow_sprite, (sprite_w, sprite_h))
        self.angle = 0
        self.in_turn = False
        self.sprite_loc = pygame.Rect(start_x, start_y, sprite_w, sprite_h)
        self.turn_direction = "RIGHT"

        self.sprite.set_colorkey((0,0,255))

    # go forward based on angle (since start angle has been changed to 0 this will have to change)
    def forward(self, step=VEL, in_turn=False):
        theta_rad = (self.angle - 90) * (math.pi / 180)
        self.sprite_loc.x += step * math.cos(theta_rad)
        self.sprite_loc.y -= step * math.sin(theta_rad)
        if not in_turn:
            self.win.blit(self.sprite, (self.sprite_loc.x, self.sprite_loc.y))

    # Rotating using the original top left corner of the image as the axis, we don't like this
    def rotate_sprite(self, turn_angle, right=True):
        """print("Before", self.angle)
        if not right:
            angle *= -1

        # naively update angle attribute
        self.angle += angle

        # handle angle greater than or equal to 360 case
        if self.angle > 359:
            self.angle = self.angle % 360

        # handle negative angle case
        elif self.angle < 0:
            self.angle = 360 + self.angle

        print("After", self.angle)

        # Perform rotation operation on sprite
        self.sprite = pygame.transform.rotate(self.sprite, self.angle - 90)"""
        if not right:
            turn_angle *= -1
        self.angle += turn_angle
        mx, my = self.sprite_loc.x, self.sprite_loc.y
        img_copy = pygame.transform.rotate(self.sprite, self.angle)

        w_center, h_center = int(img_copy.get_width() / 2), int(img_copy.get_height() / 2)
        self.win.blit(img_copy, (mx - w_center, my - h_center))

    def forward_and_turn(self):
        self.forward(-10, in_turn=True)
        self.rotate_sprite(10)

    def update_loc(self):
        self.forward_and_turn()
        # self.win.blit(self.sprite, (self.sprite_loc.x, self.sprite_loc.y))

        # self.forward()

    def in_outer_padding(self, padding=OUTER_PADDING, canvas_w=CANVAS_WIDTH, canvas_h=CANVAS_HEIGHT,
                         sprite_w=SPRITE_W, sprite_h=SPRITE_H):
        nose_x, nose_y = self.define_tip(sprite_w, sprite_h)
        """return self.sprite_loc.x <= padding or self.sprite_loc.x >= canvas_w - padding \
               or self.sprite_loc.y <= padding or self.sprite_loc.y >= canvas_h - padding"""
        return nose_x <= padding or nose_x >= canvas_w - padding or \
               nose_y <= padding or nose_y >= canvas_h - padding

    def in_inner_padding(self, padding=OUTER_PADDING, thickness=INNER_PADDING_THICKNESS,
                         canvas_w=CANVAS_WIDTH, canvas_h=CANVAS_HEIGHT,
                         sprite_w=SPRITE_W, sprite_h=SPRITE_H):
        return not self.in_outer_padding() and self.in_outer_padding(padding=padding + thickness)

import math
import numpy as np
import pygame
import os


class Fish:
    VEL = 2
    OUTER_PADDING, INNER_PADDING_THICKNESS = 50, 5
    CANVAS_WIDTH, CANVAS_HEIGHT = 900, 500
    START_X, START_Y = 400, 200
    SPRITE_H, SPRITE_W = 40, 40

    def __init__(self, sprite_w=SPRITE_W, sprite_h=SPRITE_H, start_x=START_X, start_y=START_Y, start_vel=VEL):
        arrow_sprite = pygame.image.load(os.path.join('assets', 'arrow.png'))

        self.sprite = pygame.transform.scale(arrow_sprite, (sprite_w, sprite_h))
        self.angle = 90
        self.in_turn = False
        self.sprite_loc = pygame.Rect(start_x, start_y, sprite_w, sprite_h)
        self.prev_x_vel = start_vel
        self.prev_y_vel = start_vel
        self.turn_counter = 1
        self.final_angle = 1
        self.turn_direction = "RIGHT"

    # go forward based on angle
    def forward(self, step=VEL):
        theta_rad = self.angle * (math.pi / 180)
        self.sprite_loc.x += step * math.cos(theta_rad)
        self.sprite_loc.y -= step * math.sin(theta_rad)

    # determines which kind of turn needs to be executed
    def determine_turn_info(self, padding=OUTER_PADDING, thickness=INNER_PADDING_THICKNESS, canvas_w=CANVAS_WIDTH):
        if self.sprite_loc.x < padding + thickness or self.sprite_loc.x > canvas_w - (padding + thickness):
            self.get_x_turn_info()
        else:
            self.get_y_turn_info()

    def get_x_turn_info(self):
        n = self.angle
        if self.get_quadrant() in [1, 3]:
            self.final_angle = (n + 90) % 360
            self.turn_direction = "LEFT"
        else:
            if n - 90 < 0:
                self.final_angle = 360 - (n - 90)
            else:
                self.final_angle = n - 90
            self.turn_direction = "RIGHT"

    def get_y_turn_info(self):
        n = self.angle
        self.final_angle = 360 - n
        if self.get_quadrant() in [1, 4]:
            self.turn_direction = "RIGHT"
        else:
            self.turn_direction = "LEFT"

    # determine quadrant of angle
    def get_quadrant(self):
        theta = self.angle % 360
        if theta % 90 == 0:
            return 0
        return (theta // 90) + 1

    def execute_turn(self, step=VEL, angle_step=1):
        if self.turn_counter < self.final_angle:
            self.rotate_sprite(angle_step, self.turn_direction == "RIGHT")
            self.forward(step)
            self.turn_counter += angle_step
        else:
            self.in_turn = not self.in_turn

    # Rotating using the original top left corner of the image as the axis, we don't like this
    def rotate_sprite(self, angle, right=True):
        print("Before", self.angle)
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
        self.sprite = pygame.transform.rotate(self.sprite, angle)

    # STRATEGY IS IN PLACE FIGURE OUT HOW TO DEAL WITH COORDINATE SYSTEM BEING NON-CARTESIAN
    # THIS MAY BE ACCOMPLISHED BY THEN INVERTING OVER THE Y=self.sprite_loc.y TO ACCOUNT FOR Y
    def define_tip(self, sprite_w=SPRITE_W, sprite_h=SPRITE_H):
        theta = self.angle * (math.pi / 180)
        x_up = self.sprite_loc.x + (math.cos(theta) * sprite_w) - (math.sin(theta) * (sprite_h / 2))
        y_up = self.sprite_loc.y - (math.sin(theta) * sprite_w) - (math.cos(theta) * (sprite_h / 2))

        return x_up, y_up

    def update_loc(self):
        """if not self.in_outer_padding() and self.in_inner_padding() and not self.in_turn:
            print("HERE")
            self.in_turn = True
            self.determine_turn_info()

        if self.in_turn:
            self.execute_turn()
        else:
            self.forward()"""

        self.forward()

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

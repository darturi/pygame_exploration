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
        arrow_sprite = pygame.image.load(os.path.join('../assets', 'arrow.png')).convert()

        self.win = window
        self.sprite = pygame.transform.scale(arrow_sprite, (sprite_w, sprite_h))
        self.angle = 0
        self.in_turn = False
        self.sprite_loc = pygame.Rect(start_x, start_y, sprite_w, sprite_h)
        self.turn_direction = "RIGHT"

        self.sprite.set_colorkey((0,0,255))

    # go forward based on angle (since start angle has been changed to 0 this will have to change)
    #def forward(self, step=VEL, in_turn=False):
    #    theta_rad = (self.angle - 90) * (math.pi / 180)
    #    self.sprite_loc.x += step * math.cos(theta_rad)
    #    self.sprite_loc.y -= step * math.sin(theta_rad)
    #    if not in_turn:
    #        self.win.blit(self.sprite, (self.sprite_loc.x, self.sprite_loc.y))

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
        # not sure if x should be - or +

        # self.sprite = img_copy
        # self.sprite_loc.x, self.sprite_loc.y = mx - w_center, my - h_center

        self.win.blit(img_copy, (mx - w_center, my - h_center))

    def get_future_center(self, step=VEL, angle_step=0):
        current_x, current_y = self.get_center()
        theta_rad = (self.angle + angle_step - 90) * (math.pi / 180)
        # print(current_x, ",", current_y, end=" ---> ")
        current_x += step * math.cos(theta_rad)
        current_y -= step * math.sin(theta_rad)
        # print(current_x,  ",", current_y, end=" ---> \n")
        return current_x, current_y

    def forward_to_next_center(self, step=VEL, in_turn=False, angle_step=0):
        current_center_x, current_center_y = self.get_center()
        next_center_x, next_center_y = self.get_future_center(step=step, angle_step=angle_step)
        x_diff, y_diff = round(current_center_x - next_center_x), round(current_center_y - next_center_y)

        # print(current_center_x, current_center_y, "---", next_center_x, next_center_y, "---", x_diff, y_diff, "---", self.sprite_loc.x, self.sprite_loc.y)

        self.sprite_loc.x += x_diff
        self.sprite_loc.y += y_diff

        if not in_turn:
            self.win.blit(self.sprite, (self.sprite_loc.x, self.sprite_loc.y))
        """self.sprite_loc.x, self.sprite_loc.y = self.derive_axis_from_center(step=step)
        print(self.sprite_loc.x, ",", self.sprite_loc.y)
        if not in_turn:
            self.win.blit(self.sprite, (self.sprite_loc.x, self.sprite_loc.y))

    def derive_axis_from_center(self, step=VEL):
        # center_x, center_y = self.get_future_center(step=step)
        center_x, center_y = self.get_future_center(step=step)
        theta_rad = (self.angle - 90) * (math.pi / 180)
        center_x += step * math.cos(theta_rad)
        center_y -= step * math.sin(theta_rad)
        return center_x, center_y"""

    def get_center(self, w=SPRITE_W, h=SPRITE_H):
        """mx, my = self.sprite_loc.x, self.sprite_loc.y
        w_center, h_center = int(self.sprite.get_width() / 2), int(self.sprite.get_height() / 2)
        return mx + w_center, my - h_center"""
        theta = self.angle * (math.pi / 180)

        current_center_x = self.sprite_loc.x + (math.cos(theta) * (w / 2)) - (math.sin(theta) * (h / 2))
        current_center_y = self.sprite_loc.y - (math.sin(theta) * (w / 2)) - (math.cos(theta) * (h / 2))

        return current_center_x, current_center_y

    """def forward_and_turn(self, w=SPRITE_W, h=SPRITE_H):
        #self.get_future_center()
        self.forward_to_next_center(60, in_turn=True)
        self.rotate_sprite(6)
        # input()"""

    def do_circle(self, radius):
        circumference = 2 * math.pi * radius
        step = circumference / 180
        self.forward_to_next_center(step=step, in_turn=True, angle_step=2)
        self.rotate_sprite(2)

    def update_loc(self):
        self.forward_to_next_center()
        if not self.in_outer_padding() and self.in_inner_padding():
            print("HERE")
        # self.win.blit(self.sprite, (self.sprite_loc.x, self.sprite_loc.y))

        # self.forward()

    def in_outer_padding(self, padding=OUTER_PADDING, canvas_w=CANVAS_WIDTH, canvas_h=CANVAS_HEIGHT):
        c_x, c_y = self.get_center()
        """return self.sprite_loc.x <= padding or self.sprite_loc.x >= canvas_w - padding \
               or self.sprite_loc.y <= padding or self.sprite_loc.y >= canvas_h - padding"""
        return c_x <= padding or c_x >= canvas_w - padding or c_y <= padding or c_y >= canvas_h - padding

    def in_inner_padding(self, padding=OUTER_PADDING, thickness=INNER_PADDING_THICKNESS,
                         canvas_w=CANVAS_WIDTH, canvas_h=CANVAS_HEIGHT,
                         sprite_w=SPRITE_W, sprite_h=SPRITE_H):
        return not self.in_outer_padding() and self.in_outer_padding(padding=padding + thickness)

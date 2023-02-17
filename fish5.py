import math
import pygame
import os


class Fish:
    VEL = 2
    # OUTER_PADDING, INNER_PADDING_THICKNESS = 50, 2
    CANVAS_WIDTH, CANVAS_HEIGHT = 900, 500
    # START_X, START_Y = 400, 200
    SPRITE_W, SPRITE_H = 40, 40

    def __init__(self, window, motion_path, img_path="assets/arrow.png",
                 sprite_w=SPRITE_W, sprite_h=SPRITE_H, canvas_h=CANVAS_HEIGHT, canvas_w=CANVAS_WIDTH):
        # Define sprite width and height
        self.sprite_w = sprite_w
        self.sprite_h = sprite_h

        # Load image to be sprite
        arrow_sprite = pygame.image.load(img_path).convert()

        # Define Window
        self.win = window

        # Size sprite appropriately
        self.sprite = pygame.transform.scale(arrow_sprite, (sprite_w, sprite_h))

        # Initialize start angle
        self.angle = 0

        # Initialize path
        self.path = motion_path
        self.path_stack = motion_path[1:]

        # Initialize start positition of sprite
        self.sprite_loc = pygame.Rect(motion_path[0], canvas_h - sprite_h, sprite_w, sprite_h)

        """# turn related attributes
        self.final_angle = None
        self.in_turn = False"""

        self.sprite.set_colorkey((0,0,255))

    def rotate_sprite(self, turn_angle, right=True):
        if right:
            turn_angle *= -1
        self.angle += turn_angle
        # self.angle %= 361
        mx, my = self.sprite_loc.x, self.sprite_loc.y
        img_copy = pygame.transform.rotate(self.sprite, self.angle)

        w_center, h_center = int(img_copy.get_width() / 2), int(img_copy.get_height() / 2)

        self.win.blit(img_copy, (mx - w_center, my - h_center))

    def get_future_center(self, step=VEL, angle_step=0):
        current_x, current_y = self.get_center()
        theta_rad = (self.angle + angle_step - 90) * (math.pi / 180)
        current_x += step * math.cos(theta_rad)
        current_y -= step * math.sin(theta_rad)
        return current_x, current_y

    def forward_to_next_center(self, step=VEL, in_turn=False, angle_step=0):
        current_center_x, current_center_y = self.get_center()
        next_center_x, next_center_y = self.get_future_center(step=step, angle_step=angle_step)
        x_diff, y_diff = round(current_center_x - next_center_x), round(current_center_y - next_center_y)

        self.sprite_loc.x += x_diff
        self.sprite_loc.y += y_diff

        if not in_turn:
            self.win.blit(self.sprite, (self.sprite_loc.x, self.sprite_loc.y))

    def get_center(self, w=SPRITE_W, h=SPRITE_H):
        theta = self.angle * (math.pi / 180)
        current_center_x = self.sprite_loc.x + (math.cos(theta) * (w / 2)) - (math.sin(theta) * (h / 2))
        current_center_y = self.sprite_loc.y - (math.sin(theta) * (w / 2)) - (math.cos(theta) * (h / 2))

        return current_center_x, current_center_y

    """def do_turn(self, total_turn_angle, right=True, angle_increment=2, step=VEL):
        if not self.in_turn and not right:
            self.final_angle = self.angle + total_turn_angle
            self.in_turn = True
        elif not self.in_turn and right:
            self.final_angle = self.angle - total_turn_angle
            self.in_turn = True"""

    """if right:
            angle_increment *= -1"""

    # print(self.angle, self.final_angle, angle_increment)
    """if right and self.angle >= self.final_angle:
            # print(self.angle, self.final_angle)
            self.in_turn = False
            input()
        elif not right and self.angle <= self.final_angle:
            self.in_turn = False
            input()"""

    """if abs(math.cos(math.radians(self.angle)) - math.cos(math.radians(self.final_angle))) < 0.02 and \
                abs(math.sin(math.radians(self.angle)) - math.sin(math.radians(self.final_angle))) < 0.02:
            self.in_turn = False
            input()

        self.forward_to_next_center(step=step, in_turn=True, angle_step=angle_increment)
        self.rotate_sprite(angle_increment, right=right)"""


    """def do_circle(self, radius):
        circumference = 2 * math.pi * radius
        step = circumference / 180
        self.forward_to_next_center(step=step, in_turn=True, angle_step=2)
        self.rotate_sprite(2)"""

    def follow_path(self, y_vel=VEL):
        if len(self.path_stack) > 0:
            next_x = self.path_stack.pop(0)

            self.sprite_loc.x = next_x
            self.sprite_loc.y -= y_vel

            self.win.blit(self.sprite, (self.sprite_loc.x, self.sprite_loc.y))


    def update_loc(self):
        self.follow_path(y_vel=5)
        #self.do_turn(340, right=True)
        #if not self.in_outer_padding() and self.in_inner_padding():
        #    print("HERE")
        # self.win.blit(self.sprite, (self.sprite_loc.x, self.sprite_loc.y))

        # self.forward()

    """def in_outer_padding(self, padding=OUTER_PADDING, canvas_w=CANVAS_WIDTH, canvas_h=CANVAS_HEIGHT):
        c_x, c_y = self.get_center()
        return c_x <= padding or c_x >= canvas_w - padding or c_y <= padding or c_y >= canvas_h - padding

    def in_inner_padding(self, padding=OUTER_PADDING, thickness=INNER_PADDING_THICKNESS,
                         canvas_w=CANVAS_WIDTH, canvas_h=CANVAS_HEIGHT,
                         sprite_w=SPRITE_W, sprite_h=SPRITE_H):
        return not self.in_outer_padding() and self.in_outer_padding(padding=padding + thickness)"""

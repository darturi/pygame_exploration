import math
import pygame
import os


class Fish:
    VEL = 2
    OUTER_PADDING, INNER_PADDING_THICKNESS = 50, 2
    CANVAS_WIDTH, CANVAS_HEIGHT = 900, 500
    START_X, START_Y = 400, 200
    SPRITE_H, SPRITE_W = 40, 40

    def __init__(self, window, sprite_w=SPRITE_W, sprite_h=SPRITE_H, start_x=START_X, start_y=START_Y, start_vel=VEL):
        arrow_sprite = pygame.image.load(os.path.join('../assets', 'arrow.png')).convert()

        self.win = window
        self.sprite = pygame.transform.scale(arrow_sprite, (sprite_w, sprite_h))
        self.angle = 90
        self.in_turn = False
        self.sprite_loc = pygame.Rect(start_x, start_y, sprite_w, sprite_h)
        self.prev_x_vel = start_vel
        self.prev_y_vel = start_vel
        self.turn_counter = 1
        self.final_angle = 1
        self.turn_direction = "RIGHT"

        self.sprite.set_colorkey((0,0,255))

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
        self.sprite = pygame.transform.rotate(self.sprite, self.angle - 90)

    # Gives coordinate of the tip of the sprite rather than the bottom left corner (from default)
    def define_tip(self, sprite_w=SPRITE_W, sprite_h=SPRITE_H):
        theta = self.angle * (math.pi / 180)
        x_up = self.sprite_loc.x + (math.cos(theta) * sprite_w) - (math.sin(theta) * (sprite_h / 2))
        y_up = self.sprite_loc.y - (math.sin(theta) * sprite_w) - (math.cos(theta) * (sprite_h / 2))

        return x_up, y_up

    def find_turn_axis(self, turn_angle, sprite_w=SPRITE_W, sprite_h=SPRITE_H, right=True, step=VEL):
        # define where the hilt is before the next rotation
        theta = self.angle * (math.pi / 180)
        prev_hilt_x = (sprite_w / 2) * math.cos(theta)
        prev_hilt_y = (sprite_w / 2) * math.sin(theta)

        # record turn distance
        if right:
            turn_distance = self.angle + turn_angle
        else:
            turn_distance = self.angle - turn_angle

        # Actually turn
        self.rotate_sprite(turn_angle, right)

        # calculate where the hilt will be
        theta_prime = (self.angle * (math.pi / 180))
        post_hilt_x = (sprite_w / 2) * math.cos(theta_prime)
        post_hilt_y = (sprite_w / 2) * math.sin(theta_prime)

        # Calculate necessary move justification
        x_justify = prev_hilt_x - post_hilt_x
        y_justify = prev_hilt_y - post_hilt_y

        print("Turn Info:")
        print("prev_hilt_x, prev_hilt_y", prev_hilt_x, prev_hilt_y)
        print("post_hilt_x, post_hilt_y", post_hilt_x, post_hilt_y)
        print("x_justify, y_justify", x_justify, y_justify)

        # implement justification
        """# +x, -y if turn angle in Q1 or Q3
        if (0 < turn_distance <= 90) or (270 < turn_distance <= 360):
            self.sprite_loc.x += x_justify
            self.sprite_loc.y -= y_justify
        # +x, +y if turn angle in Q2 or Q3
        else:
            self.sprite_loc.x += x_justify
            self.sprite_loc.y -= y_justify"""

    def centered_rotate(self, angle, right=True):
        print("Before", self.angle)
        if not right:
            angle *= -1

        # naively update angle attribute
        self.angle += angle

        """# handle angle greater than or equal to 360 case
        if self.angle > 359:
            self.angle = self.angle % 360

        # handle negative angle case
        elif self.angle < 0:
            self.angle = 360 + self.angle"""

        print("After", self.angle)



        # Create image copy to get current dimensions
        img_copy = pygame.transform.rotate(self.sprite, self.angle - 90)
        w_center, h_center = int(img_copy.get_width() / 2), int(img_copy.get_height() / 2)
        self.win.blit(self.sprite, (self.sprite_loc.x - w_center, self.sprite_loc.y - h_center))


    def get_sprite_center(self):
        return


    def update_loc(self):
        if not self.in_outer_padding() and self.in_inner_padding() and not self.in_turn:
            print("HERE")
        """
            self.in_turn = True
            self.determine_turn_info()

        if self.in_turn:
            self.execute_turn()
        else:
            self.forward()"""
        self.rotate_sprite(5)
        self.win.blit(self.sprite, (self.sprite_loc.x, self.sprite_loc.y))

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

import pygame
import random

class ItemManager:
    def __init__(self):
        self.shoes_img = pygame.transform.scale(pygame.image.load("./shoe.png").convert_alpha(), (50, 50))
        self.spray_img = pygame.transform.scale(pygame.image.load("./spray.png").convert_alpha(), (50, 50))

        self.item_positions = [
            (620, 150),
            (760, 150)
        ]

        self.shoes_duration = 20000
        self.spray_duration = 20000
        self.speed_boost = 2

        self.reset()

    def reset(self):
        shoes_pos, spray_pos = random.sample(self.item_positions, 2)

        self.shoes_rect = pygame.Rect(shoes_pos[0], shoes_pos[1], 50, 50)
        self.spray_rect = pygame.Rect(spray_pos[0], spray_pos[1], 50, 50)

        self.shoes_used = False
        self.spray_used = False

        self.shoes_active = False
        self.spray_active = False

        self.shoes_start_time = 0
        self.spray_start_time = 0

    def draw(self, screen):
        if not self.shoes_used:
            screen.blit(self.shoes_img, self.shoes_rect)

        if not self.spray_used:
            screen.blit(self.spray_img, self.spray_rect)

    def update(self, player_rect, base_speed, current_time):
        player_center = player_rect.center

        shoes_center_area = pygame.Rect(0, 0, 20, 20)
        shoes_center_area.center = self.shoes_rect.center

        spray_center_area = pygame.Rect(0, 0, 20, 20)
        spray_center_area.center = self.spray_rect.center

        if not self.shoes_used and shoes_center_area.collidepoint(player_center):
            self.shoes_used = True
            self.shoes_active = True
            self.shoes_start_time = current_time

        if not self.spray_used and spray_center_area.collidepoint(player_center):
            self.spray_used = True
            self.spray_active = True
            self.spray_start_time = current_time

        if self.shoes_active:
            if current_time - self.shoes_start_time >= self.shoes_duration:
                self.shoes_active = False

        if self.spray_active:
            if current_time - self.spray_start_time >= self.spray_duration:
                self.spray_active = False

        if self.shoes_active:
            return base_speed + self.speed_boost
        else:
            return base_speed

    def is_invisible(self):
        return self.spray_active
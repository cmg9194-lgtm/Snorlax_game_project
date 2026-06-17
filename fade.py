import pygame

class Fade:
    def __init__(self, width, height, speed=8):
        self.width = width
        self.height = height

        self.alpha = 0
        self.speed = speed
        self.active = False

        self.surface = pygame.Surface((width, height))
        self.surface.fill((0, 0, 0))

    def start(self, fade_in=True):
        """
        fade_in=True  → 검정 → 밝아짐 (페이드 인)
        fade_in=False → 밝음 → 검정 (페이드 아웃)
        """
        self.active = True

        if fade_in:
            self.alpha = 255
            self.direction = -1
        else:
            self.alpha = 0
            self.direction = 1

    def update(self, screen):
        if not self.active:
            return

        self.alpha += self.speed * self.direction

        if self.alpha <= 0:
            self.alpha = 0
            self.active = False

        if self.alpha >= 255:
            self.alpha = 255
            self.active = False

        self.surface.set_alpha(self.alpha)
        screen.blit(self.surface, (0, 0))

    def is_active(self):
        return self.active
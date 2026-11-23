import pygame
from src import config

class Counter:
    def __init__(self, x, y, width, total):
        self.center_x = x + width // 2
        self.rect = pygame.Rect(self.center_x - (width - 40) // 2, y, width - 40, 32)
        self.color = config.SURFACE
        self.bar_width = width
        self.total = total
        self.font = pygame.font.Font("assets/fonts/LexendDeca-Medium.ttf", 15)
        self.index = 0

        self.progress = 0
        self.target_progress = 0
        self.speed = 5

        self.active = False
        self.input_text = ''

    def update(self, index):
        self.index = index
        self.target_progress = (index + 1) / self.total

    def handle_click(self, pos):
        self.active = self.rect.collidepoint(pos)

        if self.active:
            self.input_text = ''
            self.color = config.SURFACE_HOVER
        else:
            self.color = config.SURFACE

    def animate(self, dt):
        difference = self.target_progress - self.progress
        self.progress += difference * self.speed * dt

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            (self.color),
            self.rect,
            border_radius=16
        )

        current_value = self.input_text if self.active else str(self.index + 1)

        if self.active and not current_value:
            current_value = "_"

        current_text = self.font.render(
            current_value,
            True,
            config.ACCENT if self.active else config.WHITE
        )

        total_text = self.font.render(
            f" / {self.total}",
            True,
            config.TEXT_SECONDARY
        )

        current_rect = current_text.get_rect()
        total_rect = total_text.get_rect()

        combined_width = current_rect.width + total_rect.width

        current_rect.midleft = (
            self.rect.centerx - combined_width // 2,
            self.rect.centery
        )

        total_rect.midleft = current_rect.midright

        surface.blit(current_text, current_rect)
        surface.blit(total_text, total_rect)

        bar_bg = pygame.Rect(
            self.center_x - self.bar_width // 2,
            self.rect.bottom + 6,
            self.bar_width,
            4
        )

        pygame.draw.rect(surface, (config.BORDER), bar_bg, border_radius=3)

        bar_width = int(bar_bg.width * self.progress)

        pygame.draw.rect(
            surface,
            (config.WHITE),
            (bar_bg.x, bar_bg.y, bar_width, bar_bg.height),
            border_radius=3
        )

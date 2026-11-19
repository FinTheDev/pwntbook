import pygame

class Button:
    def __init__(self, x, y, icon, action, size=48):
        self.rect = pygame.Rect(x, y, size, size)
        self.icon = pygame.transform.smoothscale(icon, (32, 32))
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        hovered = self.rect.collidepoint(mouse_pos)

        color = (65, 65, 65) if hovered else (45, 45, 45)

        pygame.draw.rect(surface, color, self.rect, border_radius=12)

        icon_rect = self.icon.get_rect(center=self.rect.center)
        surface.blit(self.icon, icon_rect)

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

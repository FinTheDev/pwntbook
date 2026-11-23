import pygame
import json
from src.icons import load_icons
from src.counter import Counter

pygame.init()

WIDTH, HEIGHT = 500, 350

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pwntbook")

clock = pygame.time.Clock()

BACKGROUND = (13, 17, 23)
ACCENT = (106, 126, 245)
TEXT = (240, 240, 240)

TEXT_SECONDARY = (130, 130, 130)
SURFACE = (30, 35, 43)
SURFACE_HOVER = (45, 52, 65)
BORDER = (48, 54, 61)
WHITE = (255, 255, 255)

flip_icon, shuffle_icon, left_icon, right_icon = load_icons()

word_font = pygame.font.Font("assets/fonts/LexendDeca-Regular.ttf", 46)
def_font = pygame.font.Font("assets/fonts/LexendDeca-Regular.ttf", 28)

with open("assets/cards.json", "r") as file:
    cards = json.load(file)

if not cards:
    with open("assets/demo.json", "r") as file:
        cards = json.load(file)

index = 0
flipped = False
shuffled = False
definition_index = 0
definition_button_rect = None

counter = Counter(WIDTH // 2 - 60, 10, 120, len(cards))

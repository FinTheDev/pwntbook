import pygame
from src import config
from src.draw import *
from src.ui import *
from src.events import handle_events
from src.cards import update_card

update_card()

running = True

while running:
    dt = config.clock.tick(60) / 1000

    running = handle_events()

    show_back = config.flipped

    config.screen.fill(config.BACKGROUND)

    if show_back:
        draw_definitions()
    else:
        config.definition_button_rect = None
        draw_word()

    config.counter.animate(dt)
    config.counter.draw(config.screen)

    flip_button.draw(config.screen)
    shuffle_button.draw(config.screen)
    left_button.draw(config.screen)
    right_button.draw(config.screen)

    pygame.display.flip()

pygame.quit()

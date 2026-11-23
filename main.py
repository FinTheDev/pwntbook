import pygame
from src import config
from src.cards import *
from src.draw import *
from src.ui import *

update_card()

running = True

while running:
    dt = config.clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if config.counter.active:
                if event.key == pygame.K_ESCAPE:
                    config.counter.active = False
                    config.counter.input_text = ''
                    config.counter.color = config.SURFACE

                elif event.key == pygame.K_RETURN:
                    if config.counter.input_text.isdigit():
                        number = int(config.counter.input_text)

                        if 1 <= number <= config.counter.total:
                            config.index = number - 1
                            update_card()

                    config.counter.active = False
                    config.counter.input_text = ''
                    config.counter.color = config.SURFACE

                elif event.key == pygame.K_BACKSPACE:
                    config.counter.input_text = config.counter.input_text[:-1]

                elif event.unicode.isdigit():
                    config.counter.input_text += event.unicode

            elif event.key == pygame.K_ESCAPE:
                running = False
                
            elif event.key == pygame.K_SPACE and event.mod & pygame.KMOD_CTRL:
                shuffle_cards()

            elif event.key == pygame.K_SPACE:
                flip_card()

            elif event.key == pygame.K_RIGHT:
                next_card()

            elif event.key == pygame.K_LEFT:
                previous_card()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if config.definition_button_rect and config.definition_button_rect.inflate(20, 12).collidepoint(event.pos):
                definitions = config.cards[config.index]["def"]

                if isinstance(definitions, list):
                    config.definition_index = (
                        config.definition_index + 1
                    ) % len(definitions)

            flip_button.click(event.pos)
            shuffle_button.click(event.pos)
            left_button.click(event.pos)
            right_button.click(event.pos)

            config.counter.handle_click(event.pos)

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

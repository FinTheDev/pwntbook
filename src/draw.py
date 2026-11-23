import pygame
from src import config

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()

        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

def draw_word():
    word = config.cards[config.index]["word"]

    lines = wrap_text(word, config.word_font, 400)
    line_height = config.word_font.get_linesize()

    total_height = len(lines) * line_height
    y = 160 - total_height // 2

    for line in lines:
        text_surface = config.word_font.render(
            line, True, (config.WHITE)
        )

        text_rect = text_surface.get_rect(
            center=(config.WIDTH // 2, y + line_height // 2)
        )

        config.screen.blit(text_surface, text_rect)
        y += line_height

def draw_definitions():
    definitions = config.cards[config.index]["def"]

    if isinstance(definitions, str):
        definitions = [{"type": "", "meaning": definitions}]

    definition = definitions[config.definition_index]

    label = definition.get("type", "")
    meaning = definition["meaning"]

    lines = wrap_text(meaning, config.def_font, 400)
    line_height = config.def_font.get_linesize()

    button_size = 48
    gap = 15

    if label:
        counter_bottom = 60

        config.definition_button_rect = pygame.Rect(
            (config.WIDTH - button_size) // 2,
            counter_bottom + gap,
            button_size,
            button_size
        )

        hovered = config.definition_button_rect.collidepoint(
            pygame.mouse.get_pos()
        )

        button_color = (config.SURFACE_HOVER) if hovered else (config.SURFACE)

        pygame.draw.rect(
            config.screen,
            button_color,
            config.definition_button_rect,
            border_radius=12
        )

        label_surface = config.def_font.render(
            label, True, (config.WHITE)
        )

        label_rect = label_surface.get_rect(
            center=config.definition_button_rect.center
        )

        config.screen.blit(label_surface, label_rect)

        y = config.definition_button_rect.bottom + gap

    else:
        config.definition_button_rect = None
        total_height = len(lines) * line_height
        y = (325 - total_height) // 2

    for line in lines:
        text_surface = config.def_font.render(
            line, True, (config.WHITE)
        )

        text_rect = text_surface.get_rect(
            center=(config.WIDTH // 2, y + line_height // 2)
        )

        config.screen.blit(text_surface, text_rect)
        y += line_height

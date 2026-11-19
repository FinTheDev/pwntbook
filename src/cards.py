import random
import json
from src import config

def update_card():
    config.flipped = False
    config.definition_index = 0
    config.counter.update(config.index)

def flip_card():
    config.flipped = not config.flipped

def shuffle_cards():
    if config.shuffled:
        with open("assets/cards.json", "r") as file:
            config.cards = json.load(file)

        config.shuffled = False
        config.index = 0
    else:
        random.shuffle(config.cards)
        config.index = 0
        config.shuffled = True

    update_card()

def next_card():
    config.index = (config.index + 1) % len(config.cards)
    update_card()

def previous_card():
    config.index = (config.index - 1) % len(config.cards)
    update_card()

from src import config
from src.button import Button
from src.cards import *

flip_button = Button(226, 285, config.flip_icon, flip_card)
shuffle_button = Button(20, 285, config.shuffle_icon, shuffle_cards)
left_button = Button(155, 285, config.left_icon, previous_card)
right_button = Button(297, 285, config.right_icon, next_card)

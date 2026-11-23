import pyconify
import cairosvg
import io
import pygame

flip_svg = pyconify.svg("eva:flip-2-fill")
shuffle_svg = pyconify.svg("basil:shuffle-outline")
left_svg = pyconify.svg("akar-icons:triangle-left-fill")
right_svg = pyconify.svg("akar-icons:triangle-right-fill")

def load_icon(svg):
    svg = svg.replace(b"currentColor", b"#F0F0F0")
    svg = svg.replace(b'fill="black"', b'fill="#F0F0F0"')

    png = cairosvg.svg2png(
        bytestring=svg,
        output_width=32,
        output_height=32
    )
    return pygame.image.load(io.BytesIO(png))

flip_icon = load_icon(flip_svg)
shuffle_icon = load_icon(shuffle_svg)
left_icon = load_icon(left_svg)
right_icon = load_icon(right_svg)

def load_icons():
    return flip_icon, shuffle_icon, left_icon, right_icon

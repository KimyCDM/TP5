"""
tp 5
Par Yul Kim
Groupe:405
dessin avec arcade
"""
import random

import arcade

SCREEN_WIDTH = 728
SCREEN_HEIGHT = 766
WINDOW_TITLE = "Pizza"


def drawing():
    arcade.set_background_color(arcade.color.WHITE)
    # pain
    arcade.draw_arc_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 300, 4500, 1200, arcade.color.LIGHT_BROWN, 84, 100)
    # fromage
    arcade.draw_triangle_filled(48, 650, 680, 650, 366, 80, arcade.color.DARK_ORANGE)
    # peperoni
    arcade.draw_arc_filled(540, SCREEN_HEIGHT / 2 + 20, 100, 100, arcade.csscolor.RED, 80, 260, 18)
    arcade.draw_circle_filled(400, 465, 50, arcade.color.RED)
    arcade.draw_circle_filled(380, 280, 50, arcade.color.RED)
    arcade.draw_circle_filled(200, 580, 50, arcade.color.RED)
    # ananas
    r = arcade.rect.XYWH(200 + 100, SCREEN_HEIGHT / 2, 30, 60)
    arcade.draw.draw_rect_filled(r, arcade.csscolor.YELLOW, random.randint(0, 360))
    r = arcade.rect.XYWH(300, 500, 30, 60)
    arcade.draw.draw_rect_filled(r, arcade.csscolor.YELLOW, random.randint(0, 360))
    r = arcade.rect.XYWH(570, 600, 30, 60)
    arcade.draw.draw_rect_filled(r, arcade.csscolor.YELLOW, random.randint(0, 360))
    r = arcade.rect.XYWH(500, 500, 30, 60)
    arcade.draw.draw_rect_filled(r, arcade.csscolor.YELLOW, random.randint(0, 360))
    r = arcade.rect.XYWH(400, 600, 30, 60)
    arcade.draw.draw_rect_filled(r, arcade.csscolor.YELLOW, random.randint(0, 360))
    # Legume
    arcade.draw_circle_outline(300, 500, 60, arcade.color.FOREST_GREEN, 4, num_segments=8,
                               tilt_angle=random.randint(0, 360))
    arcade.draw_circle_outline(400, 300, 60, arcade.color.FOREST_GREEN, 4, num_segments=8,
                               tilt_angle=random.randint(0, 360))
    arcade.draw_circle_outline(500, 450, 60, arcade.color.FOREST_GREEN, 4, num_segments=8,
                               tilt_angle=random.randint(0, 360))
    # Name
    arcade.draw_line(100, 30, 600, 30, arcade.color.BLACK)
    arcade.draw_text("PIZZA A L'ANANAS (est une crime!)", 100, 30, arcade.color.BLACK, 30)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    arcade.start_render()
    drawing()
    arcade.finish_render()
    arcade.run()


if __name__ == '__main__':
    main()

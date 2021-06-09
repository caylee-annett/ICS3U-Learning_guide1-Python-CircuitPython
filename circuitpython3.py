#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This is the "Space Aliens" program on the PyBadge

import ugame
import stage


def game_scene():
    # This function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_
                                                  background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set the background to image 0 in the image bank and the size
    #   to (10x8 tiles of 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create a stage for the background to show up on and set the frame
    #   rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers of all sprites
    game.layers = [ship] + [background]
    # render all sprites
    game.render_block()

    # Repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick() wait until refresh rate rate finishes


if __name__ == "__main__":
    game_scene()

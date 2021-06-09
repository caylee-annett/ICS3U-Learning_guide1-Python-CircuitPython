#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This is the "Space Aliens" program on the PyBadge

import ugame
import stage

import constants


def game_scene():
    # This function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_
                                                  background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set the background to image 0 in the image bank and the size
    #   to (10x8 tiles of 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75,
                        constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # create a stage for the background to show up on and set the frame
    #   rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites
    game.layers = [ship] + [background]
    # render all sprites
    game.render_block()

    # Repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + constants.SPRITE_MOUVEMENT_SPEED, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - constants.SPRITE_MOUVEMENT_SPEED, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()

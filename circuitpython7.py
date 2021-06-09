#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This is the "Space Aliens" program on the PyBadge

import ugame
import stage

import constants


def menu_scene():
    # This function is the menu scene

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(width=29, height=12, font=None,
                       palette=constants.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None,
                       palette=constants.RED_PALETTE, buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # set the background to image 0 in the image bank and the size
    #   to (10x8 tiles of 16x16)
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # create a stage for the background to show up on and set the frame
    #   rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites
    game.layers = text + [background]
    # render all sprites
    game.render_block()

    # Repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        # redraw Sprites
        game.tick()  # wait until refresh rate finishes


def game_scene():
    # This function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_
                                                  background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # set the background to image 0 in the image bank and the size
    #   to (10x8 tiles of 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75,
                        constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    alien = stage.Sprite(image_bank_sprites, 9, int(
                         constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                         16)

    # create a stage for the background to show up on and set the frame
    #   rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites
    game.layers = [ship] + [alien] + [background]
    # render all sprites
    game.render_block()

    # Repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button to fire
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        # B button
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT != 0:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + constants.SPRITE_MOUVEMENT_SPEED, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x >= 0:
                ship.move(ship.x - constants.SPRITE_MOUVEMENT_SPEED, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # update game logic
        # play sound if A was button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw Sprites
        game.render_sprites([ship] + [alien])
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    menu_scene()

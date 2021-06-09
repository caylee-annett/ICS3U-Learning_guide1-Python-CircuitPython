#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This is the "Space Aliens" program on the PyBadge

import ugame
import stage
import time
import random
import board
import neopixel

import constants


def splash_scene():
    # This function is the splash scene

    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # create a stage for the background to show up on and set the frame
    #   rate to 60fps
    # set the background to image 0 in the image bank
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # used this program to split the image into tile:
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # create a stage for the background to show up on and set the frame
    #   rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites
    game.layers = [background]
    # render all sprites
    game.render_block()

    # Repeat forever, game loop
    while True:
        # wait for 2 seconds
        time.sleep(2.0)
        menu_scene()


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
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

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
    
    # for score
    score = 0

    def show_alien():
        # this function takes an alien from off screen and moves it on screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(
                    0 + constants.SPRITE_SIZE,
                    constants.SCREEN_X - constants.SPRITE_SIZE),
                    constants.OFF_TOP_SCREEN)
                break

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16(
        "space_aliens_background.bmp")
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
    background = stage.Grid(image_bank_background, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75,
                        constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # create list of aliens
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    # place one alien on the screen
    show_alien()

    # create list of lasers for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    # create a stage for the background to show up on and set the frame
    #   rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers of all sprites
    game.layers = lasers + [ship] + aliens + [background]
    # render all sprites
    game.render_block()

    # set up Neopixel colours
    pixel_pin = board.D8
    order = neopixel.RGB
    pixel = neopixel.NeoPixel(pixel_pin, 5, pixel_order=order)
    pixel[0] = constants.GREEN
    pixel[1] = constants.GREEN
    pixel[2] = constants.GREEN
    pixel[3] = constants.GREEN
    pixel[4] = constants.GREEN

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
            # fire a laser, if all lasers are not used up
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    # change Neopixel colour to yellow
                    pixel[laser_number] = constants.YELLOW
                    break

        # each frame move the lasers that have been fired up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x,
                                          lasers[laser_number].y -
                                          constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    # change Neopixels back to green once moved back
                    pixel[laser_number] = constants.GREEN
                # change Neopixels to red if all lasers have been fired
                if lasers[0].x > 0 and lasers[1].x > 0 and lasers[2].x > 0 \
                        and lasers[3].x > 0 and lasers[4].x > 0:
                    pixel[laser_number] = constants.RED

        # each frame move the aliens down that are on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x,
                                          aliens[alien_number].y +
                                          constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    show_alien()

        # each frame check if any lasers are touching any aliens
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6,
                            lasers[laser_number].y + 2,
                            lasers[laser_number].x + 11,
                            lasers[laser_number].y + 12,
                            aliens[alien_number].x + 1,
                            aliens[alien_number].y,
                            aliens[alien_number].x + 15,
                            aliens[alien_number].y + 15):
                            # you hit an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X,
                                constants.OFF_SCREEN_Y,)
                            lasers[laser_number].move(constants.OFF_SCREEN_X,
                                constants.OFF_SCREEN_Y)
                            boom_sound = open("boom.wav", 'rb')
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1

        # redraw Sprites
        game.render_sprites(lasers + [ship] + aliens)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    splash_scene()

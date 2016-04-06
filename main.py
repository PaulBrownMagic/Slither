# add sound and buttons with keyboard selection as well as mouse.
# add continue function
# Update messages
# Sort out game states functionality
# Mazes: add rows maze with links to get through rows

import pygame
pygame.init()  # called early as it is required for constants.
from constants import *
from game_states import *


def set_state(new_state, all_states):
    for state in range(len(all_states)):
        all_states[state] = False
    all_states[new_state] = True


def update_state(current_state, game_states):
    # Delete old state
    del current_state

    # Create new state
    if game_states[GAME_PLAY]:
        current_state = GamePlay()
    elif game_states[GAME_OVER]:
        current_state = GameOver()
    return current_state


# Main game loop
def game_loop():
    game_exit = False

    # game states
    game_over = False
    game_play = False
    game_intro = True
    game_paused = False
    game_states = [game_intro, game_play, game_over, game_paused]
    game_state = GAME_INTRO
    current_state = GameIntro()

    while not game_exit:

        # Events
        current_state.event_handling()

        if game_state == GAME_PLAY:
            for event in current_state.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p and game_state != GAME_PAUSED:
                        game_paused = True

        # Game Logic
        current_state.run_logic()
        game_exit = current_state.game_exit

        # Next Level
        if game_state == GAME_PLAY:
            if current_state.score == MAX_SCORE:
                if current_state.levels.current_level < len(current_state.levels.levels):
                    current_state.levels.current_level += 1
                else:
                    current_state.levels.current_level = 0
                current_state.display_update()
                current_state.display_flip()
                game_paused = True
                current_state.snake.reset(current_state.levels.current_level)
                current_state.score = 0
                current_state.levels.get_image_map()
                current_state.levels.get_collision_map()
                current_state.apple.rand_apple_place(current_state.levels.collision_map)

        # Changing game states
        if not current_state.active:
            paused = False
            # Current state ends, find new state
            if game_state == GAME_INTRO or game_state == GAME_OVER:
                game_state = GAME_PLAY
            elif game_state == GAME_PLAY:
                if current_state.snake.game_over:
                    game_state = GAME_OVER
            elif game_state == GAME_PAUSED and game_paused:
                paused = True
            elif game_state == GAME_PAUSED and not game_paused:
                game_state = GAME_PLAY
                paused = True
            # Update list of states so only new state is True
            if not paused:
                set_state(game_state, game_states)
                current_state = update_state(current_state, game_states)
            else:
                current_state = last_state

        if game_paused:
            game_state = GAME_PAUSED
            last_state = current_state
            current_state = GamePause()
            game_paused = False

        # Display updates
        current_state.display_update()
        current_state.display_flip()

    pygame.quit()
    quit()

game_loop()

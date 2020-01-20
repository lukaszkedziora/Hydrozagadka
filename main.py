import util
import engine
import ui
from termcolor import colored, cprint
# import time           MOZE SIE PRZYDAC DO DIALOGOW

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3 

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Createrree to extend this dictionary!

    Returns:
    dictionary
    '''
  
    engine.player['player name'] = input("Please enter player's name: ")


def main():
    util.clear_screen()
    player = create_player()
    util.clear_screen()
    
    is_running = True

    while is_running:
        board = engine.create_board()
        x = engine.put_player_on_board(board)
        ui.display_board(x)
        engine.display_player_stats()
        
        key = util.key_pressed()    
        if key == 'w' or 'd' or 's' or 'a':
            engine.wsad(key, board)
            engine.dialogue()
        if key == 'q':
            is_running = False
        if key == 'h':
            engine.loose_health(40)
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()

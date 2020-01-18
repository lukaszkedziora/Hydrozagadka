import util
import engine
import ui
# import time           MOZE SIE PRZYDAC DO DIALOGOW

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3 

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:s
    dictionary
    '''
    pass


def main():
    player = create_player()
    util.clear_screen()
    is_running = True

    while is_running:
        board = engine.create_board()
        x = engine.put_player_on_board(board)
        ui.display_board(x)
        
        key = util.key_pressed()    
        if key == 'w' or 'd' or 's' or 'a':
            engine.wsad(key, board)
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()

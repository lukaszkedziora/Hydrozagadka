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

    Returns:
    dictionary
    '''
    pass


def main(): 
    player = create_player()
    
    util.clear_screen()
    is_running = True
    while is_running:
        board = engine.create_board()
        engine.put_player_on_board(board)
        ui.display_board(board)
        # ui.display_board("board1.txt")   
        # ui.display_board(ui.boards[player['board']]['file'])    #### jak zaimportowac slownik

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        if key == "w":
            engine.wsad(key)
        if key == "a":
            engine.wsad(key)
        if key == "s":
            engine.wsad(key)
        if key == "d":
            engine.wsad(key)                        
        else:
            pass                        #### wsad  keys? 
        util.clear_screen()


if __name__ == '__main__':
    main()

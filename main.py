import util
import engine
import ui
# import time           MOZE SIE PRZYDAC DO DIALOGOW


def create_player():
    engine.player['player name'] = input("Please enter player's name: ")


def main():
    util.clear_screen()
    player = create_player()
    util.clear_screen()
    
    is_running = True

    while is_running:
        engine.printing_board()
        engine.display_player_stats()
        
        key = util.key_pressed()    
        if key == 'q':
            is_running = False
        elif key == 'w' or 'd' or 's' or 'a':
            board = engine.create_board()
            engine.wsad(key, board)
            engine.dialogue()
        else:
            pass
        util.clear_screen()


 


if __name__ == '__main__':
    main()

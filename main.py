import util
import engine
import ui
from termcolor import colored, cprint
# import time           MOZE SIE PRZYDAC DO DIALOGOW


def create_player():
  
    engine.player['player name'] = input("Please enter player's name: ")
    engine.player['position'] = engine.characters[engine.boards[engine.player['board']]['characters'][0]]['position'][engine.player['board']]


def main():
    util.clear_screen()
    player = create_player()   
    util.clear_screen()
    is_running = True

    while is_running:
        ui.display_board(engine.put_player_on_board(engine.create_board(engine.player['board'])))
        engine.display_player_stats()
        
        key = util.key_pressed()    
        if engine.player['health'] > 0:
            if key == 'q':
                is_running = False
            elif key == 'w' or 'd' or 's' or 'a':
                board = engine.create_board(engine.player['board'])
                engine.wsad(key, board)
                engine.dialogue()
            else:
                pass
            util.clear_screen()  
        elif engine.player['health'] <= 0:
            util.clear_screen()
            engine.game_over()
            is_running = False
            

if __name__ == '__main__':
    main()

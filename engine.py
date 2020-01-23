import util
import ui
import random
import time


player = {
    'board': 'board1',
    'name': 'Kapitan AS',
    'player name': '',
    'health': 100,
    'status': 'Na wschodzie bez zmian!',
    'inventory': "test"                          # to do: add inventory
}

characters = {
    'jola': {
        'title': 'Pani Jola',
        'pictogram': '⚥',
        'status': True,
        'position': {
            'board1': [14, 15],
            'board2': [14, 15]
        },
        'dialogue': {
            1: 'Cześć Janku..',
            2: 'Piękna pogoda, prawda?',
            3: 'Może dlatego w całym mieście brakuje wody',
            4: 'Dlaczego miałbyś wiedzieć, to zadanie dla Asaaa, a nie takiego Pana Janka.. Uwielbiam Aaasa, ahhhh',
            5: 'Spytaj meterologa Janusza',
        },
    },
    'as': {
        'title': 'As',
        'pictogram': '@',
        'position': {
            'board1': [2, 2],
            'board2': [2, 2]
        },
        'dialogue': {
            'jola': {
                1: 'Cześć Jolu!',
                2: 'Straszna spiekota',
                3: 'Jak to brakuje wody, nic o tym nie wiem!',
                4: 'Gdzie mogę dowiedzieć się więcej?',
                5: 'Dziękuję!'
            },
            'kolega': {
                1: 'Cześć Januszu!',
                2: 'Zastanawiam się co dzisiaj powie nam Wicherek?',
                3: 'Słyszałem, że kończą się zapasy wody, czy to prawda?',
                4: 'Januszu spróbuj sobie coś przypomnieć, to dla mnie ważne',
                5: 'Co słyszałeś Januszu, szybciej, mów!',
                6: 'Będę milczał jak zaklęty, przysięga meteorologa',
                7: 'Żegnaj Januszu'
            },
            'agenci': {
                1: 'Cześć Jolu!',
                2: 'Straszna spiekota',
                3: 'Jak to brakuje wody, nic o tym nie wiem!',
                4: 'Gdzie mogę dowiedzieć się więcej?',
                5: 'Dziękuję!'
            },
            'informator': {
                1: 'Cześć Jolu!',
                2: 'Straszna spiekota',
                3: 'Jak to brakuje wody, nic o tym nie wiem!',
                4: 'Gdzie mogę dowiedzieć się więcej?',
                5: 'Dziękuję!'
            }
        }
    },
    'agenci': {
        'title': 'Agent',
        'status': False,
        'pictogram': '☭',
        'position': {
            'board1': [9, 90],
            'board2': [9, 90]

        },
        'dialogue': {
            1: 'Witaj Janku',
        }
    },
    'kolega': {
        'title': 'Meterolog Janusz',
        'pictogram': '☉',
        'status': False, 
        'position': {
            'board1': [16, 11],
            'board2': [16, 11]
        },
        'dialogue': {
            1: 'Witaj Janku',
            2: 'Co tam u Ciebie?',
            3: 'Że upał i spiekota utrzymają się do końca tygodnia',
            4: 'Te sprawy są dzisiaj ściśle tajne, nic nie wiem..',
            5: 'Słyszełm, że ..',
            6: 'Jeśli komukolwiek wygadasz, to () przysięgam!',
            7: 'Słyszałem, że Wydział II Urzędu Ochrny Wody się tym zajmuje, idź nad rzekę'
        }
    },
    'informator': {
        'title': 'Informator ',
        'status': False,
        'pictogram': '⚝',
        'position': {
            'board1': [3, 93],
            'board2': [3, 93]
        },
        'dialogue': {
            1: 'Witaj Janku',
        }
    },
    'droznik': {
        'title': 'Dróżnik',
        'status': True,
        'pictogram': '☢',
        'position': {
            'board1': [3, 93],
            'board2': [16, 29]
        },
        'dialogue': {
            1: 'Witaj Janku',
        }
    },
    'szefowa': {
        'title': 'Iga ze Złego Leszcza',
        'status': False,
        'pictogram': '🐟',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        },
        'dialogue': {
            1: 'Witaj Janku',
        }
    },
    'maharadza': {
        'title': 'Maharadża Kaburu',
        'status': False,
        'pictogram': '🐟',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        },
        'dialogue': {
            1: 'Witaj Janku',
        }
    },
    'szefowa': {
        'title': 'Iga ze Złego Leszcza',
        'status': False,
        'pictogram': '🍾',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'plama': {
        'title': 'doktur Plama',
        'status': False,
        'pictogram': '🐟',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        },
        'dialogue': {
            1: 'Witaj Janku',
        }
    },
    'bot1': {
        'title': 'bot1',
        'status': False,
        'pictogram': '🐟',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot2': {
        'title': 'bot2',
        'status': False,
        'pictogram': '🐟',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot3': {
        'title': 'bot3',
        'status': False,
        'pictogram': '🐟',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot4': {
        'title': 'bot4',
        'status': False,
        'pictogram': '🐟',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot5': {
        'title': 'bot5',
        'status': False,
        'pictogram': '🐟',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot6': {
        'title': 'bot1',
        'status': False,
        'pictogram': '🐦',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot7': {
        'title': 'bot1',
        'status': False,
        'pictogram': '🐦',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot8': {
        'title': 'bot1',
        'status': False,
        'pictogram': '🐦',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot9': {
        'title': 'bot1',
        'status': False,
        'pictogram': '🐦',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot10': {
        'title': 'bot1',
        'status': False,
        'pictogram': '🐦',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },'bot11': {
        'title': 'bot1',
        'status': False,
        'pictogram': '⛅',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot12': {
        'title': 'bot1',
        'status': False,
        'pictogram': '⛅',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot13': {
        'title': 'bot1',
        'status': False,
        'pictogram': '⛅',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot14': {
        'title': 'bot1',
        'status': False,
        'pictogram': '⛅',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
    'bot15': {
        'title': 'bot1',
        'status': False,
        'pictogram': '⛅',
        'position': {
            'board1': [3, 93],
            'board2': [8, 82]
        }
    },
}

boards = {
    'board1': {
        'title': '1',
        'items': {'Parsolka': [5, 43, '☂'],
                  'Karma': [4, 43, '☠'],
                  'Kombinezon': [3, 43, '☣']
                },
        'file': 'board1.txt',
        'river': {
            'start': 50,
            'width': 15,
            'in': '*',
            'out': '/'
        },
        'characters': ['as', 'jola', 'kolega', 'agenci', 'informator'],
        'bot': {
            'bot_fish': ['bot1', 'bot2', 'bot3', 'bot4', 'bot5'],
            'bot_sun': ['bot11', 'bot12', 'bot13', 'bot14', 'bot15'],
            'bot_bird': ['bot6', 'bot7', 'bot8', 'bot9', 'bot10']
        }
    },
    'board2': {
        'title': '2',
        'items': {'Alkohol': [5, 43, '☢'],
                  'Karma': [4, 43, '☠'],
                  'Kombinezon': [3, 43, '☂']
                },
        'file': 'board2.txt',
        'river': {
            'start': 50,
            'width': 15,
            'in': '*',
            'out': '/'
        },
        'characters': ['as', 'droznik', 'szefowa'],
        'bot': {
            'bot_fish': ['bot1', 'bot2', 'bot3', 'bot4', 'bot5']
        }  
    }
}


def create_board(current_board=player['board']):
    player['board'] = current_board
    file_name = boards[player['board']]['file']
    with open(file_name, 'r') as file:
        result2 = []
        for line in file:
            result = []
            for sign in line:
                result.append(sign)
            result2.append(result)
    return result2


def put_player_on_board(result1):
    for i in range(len(boards[player['board']]['characters'])):
        result1[characters[boards[player['board']]['characters'][i]]['position'][player['board']][0]] \
            [characters[boards[player['board']]['characters'][i]]['position'][player['board']][1]] \
            = characters[boards[player['board']]['characters'][i]]['pictogram']
    for bot_type in boards[player['board']]['bot']:
        for x in range(len(boards[player['board']]['bot'][bot_type])):          
            result1[characters[boards[player['board']]['bot'][bot_type][x]]['position'][player['board']][0]] \
                [characters[boards[player['board']]['bot'][bot_type][x]]['position'][player['board']][1]] \
                    = characters[boards[player['board']]['bot'][bot_type][x]]['pictogram']
    for key in boards[player['board']]['items']:
        items_pictogram = boards[player['board']]['items'][key][2]
        result1[boards[player['board']]['items'][key][0]][boards[player['board']]['items'][key][1]] \
            = items_pictogram
    return result1

def bot_movement():
    for bot_type in boards[player['board']]['bot']:
        for bot_name in boards[player['board']]['bot'][bot_type]:
            if bot_type == 'bot_fish':
                characters[bot_name]['position'][player['board']][0] = random.randint(15, 18)
                characters[bot_name]['position'][player['board']][1] = random.randint(59, 98)
            elif bot_type == 'bot_sun':
                characters[bot_name]['position'][player['board']][0] = random.randint(9, 18)
                characters[bot_name]['position'][player['board']][1] = random.randint(8, 21)
            elif bot_type == 'bot_bird':
                characters[bot_name]['position'][player['board']][0] = random.randint(1, 4)
                characters[bot_name]['position'][player['board']][1] = random.randint(87, 99)
    

def bot_interaction():
    player['status'] = 'Na zachodzie bez zmian'
    for bot_type in boards[player['board']]['bot']:
        for i in range(len(boards[player['board']]['bot'][bot_type])):
            if bot_type == 'bot_fish':
                if characters[boards[player['board']]['characters'][0]]['position'][player['board']] \
                     == characters[boards[player['board']]['bot']['bot_fish'][i]]['position'][player['board']]:
                    player['health'] = player['health'] - 100
                    player['status'] = 'Health - 100, zjadły Cię zmutowane leszcze!'
            elif bot_type == 'bot_sun':
                if characters[boards[player['board']]['characters'][0]]['position'][player['board']] \
                     == characters[boards[player['board']]['bot']['bot_sun'][i]]['position'][player['board']]:
                    player['health'] = player['health'] - 10
                    player['status'] = 'Health - 10, ostre słońe spiekło Ci skórę!'
                    #print('____________________________' '\n \n' 'Health - 1 ''\n''ostre słońe spiekło Ci skórę!')
                    #print('____________________________')
                    #time.sleep(.900)
                    #util.clear_screen()      
            elif bot_type == 'bot_bird':
                if characters[boards[player['board']]['characters'][0]]['position'][player['board']] \
                 == characters[boards[player['board']]['bot']['bot_bird'][i]]['position'][player['board']]:
                    player['health'] = player['health'] - 20
                    player['status'] = 'Health - 20, podziobały Cię spragnione wróble!'
         
                
      
                        
               

def wsad(key, board):      
    player_position = characters[boards[player['board']]['characters'][0]]['position'][player['board']]     # starting position in dictionary
    next_move = player_position.copy()                      # copy of player position that will be modified
    if key == "w":
        next_move[0] -= 1
    elif key == "a":
        next_move[1] -= 1
    elif key == "s":
        next_move[0] += 1
    elif key == "d":
        next_move[1] += 1
    if is_move_possible(board, next_move):                  # checks if move is possible: within board range
        player_position[0] = next_move[0]                   # and not blocked by a wall
        player_position[1] = next_move[1]


def is_move_possible(board, move):
    walls = ["|", "~", "█", "^"] 
    if move[0] < 1 or move[0] >= len(board)-1:              # is move in range height
        return False
    if move[1] < 1 or move[1] >= len(board[0])-1:           # is move in range width
        return False
    if board[move[0]][move[1]] in walls:                    # is move blocked by a wall
        return False
    return True


def is_item(board, move):
    items = []                                              # boards[player['board']]['items']
    if board[move[0]][move[1]] in items:
        pass                                                # to do: add item to inventory


def display_player_stats():
    print("+---------+", '{:>80}'.format('x'))
    print("|    ____ |  Player name: ", player['player name'],' | Status:', player['status'])      # to do: add messages if needed
    print("|   / _  ||  Level: ", boards[player['board']]['title'])
    print("|  / /_| ||  Health: ", player['health'])
    print("| / ___  ||")
    print("|/_/   |_||  Inventory: ", player['inventory'])
    print("+---------+")


def dialogue():
    i = 1
    while i != len(boards[player['board']]['characters']):
        if characters[boards[player['board']]['characters'][0]]['position'][player['board']] == characters[boards[player['board']]['characters'][i]]['position'][player['board']]:
            if characters[boards[player['board']]['characters'][i]]['status'] == True:
                ist_running = True
                x = 0
                try:
                    while ist_running:
                        util.clear_screen()
                        ui.display_board(put_player_on_board(create_board(player['board'])))
                        a = characters[boards[player['board']]['characters'][0]]['dialogue'][boards[player['board']]['characters'][i]][1+x]
                        b = characters[boards[player['board']]['characters'][i]]['title']
                        print(b + ': ' + characters[boards[player['board']]['characters'][i]]['dialogue'][1+x])
                        print(f'Odpowiedz: \n{a} (a) \nDo widzenia (d)')
                        key_input = util.key_pressed()    
                        if key_input == 'd':
                            ist_running = False
                        elif key_input == 'a':
                            x = x + 1
                            if x <= (len(characters[boards[player['board']]['characters'][0]]['dialogue'][boards[player['board']]['characters'][i]])) - 1:
                                if i < len(boards[player['board']]['characters']) - 1:
                                    characters[boards[player['board']]['characters'][i+1]]['status'] = True
                                else:
                                    player['board'] = 'board2'
                                    i = len(boards[player['board']]['characters'])-1
                                    ist_running = False
                                ui.display_board(put_player_on_board(create_board(player['board'])))
                            else:
                                break
                        else:
                            pass
                except KeyError:
                    print() # I've got nothing to say
        i = i + 1

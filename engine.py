player = {
    'board': 'board1',
    'name': 'Kapitan AS'
}

characters = {
    'jola': {
        'title': 'Pani Jola',
        'pictogram': '⚥',
        'position': {
            'board1': [16, 15]
        },
        'dialogs': {
            1: 'Cześć Janku..',
            2: 'Piękna pogoda prawda?',
            3: 'Może dlatego w całym mieście prakuje wody',
            4: 'Dlaczego miałbyś wiedzieć to zadanie dla As, a nie takiego Pana Janka..',
            5: 'Spytaj Janusza',
        },
    },
    'as': {
        'title': 'As',
        'pictogram': '@',
        'position': {
            'board1': [14, 15]
        },
        'dialogs': {
            'jola': {
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
        'pictogram': '☭',
        'position': {
            'board1': [9, 90]
        }
    },
    'kolega': {
        'title': 'Kolega Janusz',
        'pictogram': '☉',
        'position': {
            'board1': [16, 11]
        }
    },
    'informator': {
        'title': 'Informator ',
        'pictogram': '⚝',
        'position': {
            'board1': [3, 92]
        }
    }
}

boards = {
    'board1': {
        'title': 'board1',
        'items': {'Parsolka': [5, 43, '☢'],
                  'Karma': [4, 43, '☠'],
                  'Kombinezon': [3, 43, '☂']
                },
        'file': 'board1.txt',
        'river': {
            'start': 50,
            'width': 15,
            'in': '*',
            'out': '/'
        },
        'characters': ['as', 'jola', 'agenci', 'kolega', 'informator']
    }
}


def create_board(file_name=boards[player['board']]['file']):
    with open(file_name, 'r') as file:
        result2 = []
        for line in file:
            result = []
            for sign in line:
                result.append(sign)
            result2.append(result)
    return result2


def put_player_on_board(result1):
    for key in boards[player['board']]['items']:
        items_pictogram = boards[player['board']]['items'][key][2]
        result1[boards[player['board']]['items'][key][0]][boards[player['board']]['items'][key][1]] \
            = items_pictogram
    for i in range(len(boards[player['board']]['characters'])):
        result1[characters[boards[player['board']]['characters'][i]]['position'][player['board']][0]] \
            [characters[boards[player['board']]['characters'][i]]['position'][player['board']][1]] \
            = characters[boards[player['board']]['characters'][i]]['pictogram']
    return result1


def wsad(key, board):      
    player_position = characters[boards[player['board']]['characters'][0]]['position'][player['board']]
    next_move = player_position.copy()
    if key == "w":
        next_move[0] -= 1
    elif key == "a":
        next_move[1] -= 1
    elif key == "s":
        next_move[0] += 1
    elif key == "d":
        next_move[1] += 1
    if is_move_possible(board, next_move):
        player_position[0] = next_move[0]
        player_position[1] = next_move[1]


def is_move_possible(board, move):
    walls = ["|", "~", "█"] 
    if move[0] < 1 or move[0] >= len(board)-1:          
        return False
    if move[1] < 1 or move[1] >= len(board[0])-1:      
        return False
    if board[move[0]][move[1]] in walls:
        return False
    return True

#def is_item(board, move):
#    items = ["*"] 
#    if board[move[0]][move[1]] in items:
#        pass                                            # add item to inventory


def dialogs():
    i = 1
    #while i != len(boards[player['board']]['characters']):
    if characters[boards[player['board']]['characters'][0]]['position'][player['board']] == characters[boards[player['board']]['characters'][i]]['position'][player['board']]:
        print(characters[boards[player['board']]['characters'][i]]['dialogs'][1])
        is_running = True
        x = 0
        while is_running:
            a = characters[boards[player['board']]['characters'][0]]['dialogs'][boards[player['board']]['characters'][i]][1+x]
            key = input(f'Co chcesz zrobić? \n(a): {a} \n(q): wyjść \n')
            if key == 'q':
                is_running = False
            elif key == 'a':
                x = x + 1
                if x <= 4:
                    print(characters[boards[player['board']]['characters'][i]]['dialogs'][1+x])
                else:
                    break    
        i = i + 1
       

#dialogs()

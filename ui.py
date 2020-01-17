import os

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
        }
    },
    'as': {
        'title': 'As',
        'pictogram': '@',
        'position': {
            'board1': [14, 13]
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
        'characters': ['jola', 'as', 'agenci', 'kolega', 'informator']
    }
}


def display_board(file_name):
    result1 = []
    with open(file_name, 'r') as file:
        
        for line in file:
            result = []
            for sign in line:
                result.append(sign)
            result1.append(result)
    for key in boards[player['board']]['items']:
        items_pictogram = boards[player['board']]['items'][key][2]
        result1[boards[player['board']]['items'][key][0]][boards[player['board']]['items'][key][1]] = items_pictogram

    move = input("your move " )  
    walls = ["|", "O", "~", "_"]   
    if move not in walls: 
        if move == "W":
            characters[boards[player['board']]['characters'][1]]['position'][player['board']][0] -= 1
        elif move == "A":
            characters[boards[player['board']]['characters'][1]]['position'][player['board']][1] -= 4
        elif move == "S":
            characters[boards[player['board']]['characters'][1]]['position'][player['board']][0] += 1
        elif move == "D":
            characters[boards[player['board']]['characters'][1]]['position'][player['board']][1] += 1
    else:
        print("Sciana")

    for i in range(len(boards[player['board']]['characters'])):
        result1[characters[boards[player['board']]['characters'][i]]['position'][player['board']][0]] \
            [characters[boards[player['board']]['characters'][i]]['position'][player['board']][1]] \
            = characters[boards[player['board']]['characters'][i]]['pictogram']
    for row in result1:
        for cell in row:
            print(cell, end='')
    print()
    return


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


clear_screen()
display_board(boards[player['board']]['file'])
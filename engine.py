import util


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


def create_board(file_name=boards[player['board']]['file']):
    with open(file_name, 'r') as file:
        result1 = []
        for line in file:
            result = []
            for sign in line:
                result.append(sign)
            result1.append(result)
    return result1


def put_player_on_board(result1):
    for key in boards[player['board']]['items']:
        items_pictogram = boards[player['board']]['items'][key][2]
        result1[boards[player['board']]['items'][key][0]][boards[player['board']]['items'][key][1]] = items_pictogram
    for i in range(len(boards[player['board']]['characters'])):
        result1[characters[boards[player['board']]['characters'][i]]['position'][player['board']][0]] \
            [characters[boards[player['board']]['characters'][i]]['position'][player['board']][1]] \
            = characters[boards[player['board']]['characters'][i]]['pictogram']
    return result1


def wsad(key):  
    if key == "w":
        characters[boards[player['board']]['characters'][1]]['position'][player['board']][0] -= 1
    elif key == "a":
        characters[boards[player['board']]['characters'][1]]['position'][player['board']][1] -= 1
    elif key == "s":
        characters[boards[player['board']]['characters'][1]]['position'][player['board']][0] += 1
    elif key == "d":
        characters[boards[player['board']]['characters'][1]]['position'][player['board']][1] += 1


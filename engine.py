player = {
    'bord': 'bord1',
    'name': 'Kapitan AS'
}

characters = {
    'jola': {
        'titel': 'Pani Jola',
        'pictogram': '⚥',
        'position': {
            'bord1': [16, 15]
        }
    },
    'as': {
        'titel': 'As',
        'pictogram': '@',
        'position': {
            'bord1': [14, 13]
        }
    },
    'agenci': {
        'titel': 'Agent',
        'pictogram': '☭',
        'position': {
            'bord1': [9, 90]
        }
    },
    'kolega': {
        'titel': 'Kolega Janusz',
        'pictogram': '☉',
        'position': {
            'bord1': [16, 11]
        }
    },
    'informator': {
        'titel': 'Informator ',
        'pictogram': '⚝',
        'position': {
            'bord1': [3, 92]
        }
    }
}

bords = {
    'bord1': {
        'title': 'bord1',
        'items': {'Parsolka': [5, 43, '☢'],
                  'Karma': [4, 43, '☠'],
                  'Kombinezon': [3, 43, '☂']
                },
        'file': 'bord1.txt',
        'river': {
            'start': 50,
            'width': 15,
            'in': '*',
            'out': '/'
        },
        'characters': ['jola', 'as', 'agenci', 'kolega', 'informator']
    }
}


def create_board(file_name=bords[player['bord']]['file']):
    with open(file_name, 'r') as file:
        result1 = []
        for line in file:
            result = []
            for sign in line:
                result.append(sign)
            result1.append(result)
    return result1


def put_player_on_board(result1):
    for key in bords[player['bord']]['items']:
        items_pictogram = bords[player['bord']]['items'][key][2]
        result1[bords[player['bord']]['items'][key][0]][bords[player['bord']]['items'][key][1]] = items_pictogram
    for i in range(len(bords[player['bord']]['characters'])):
        result1[characters[bords[player['bord']]['characters'][i]]['position'][player['bord']][0]][characters[bords[player['bord']]['characters'][i]]['position'][player['bord']][1]] = characters[bords[player['bord']]['characters'][i]]['pictogram']
    return result1

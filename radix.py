to_char = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}


def convert_number(number, radix):
    converted = ''
    while number >= radix:
        number, mod = divmod(number, radix)
        converted = to_char[mod] + converted

    converted = to_char[number] + converted
    return converted


closed_spaces = {
    '0': 1,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 1,
    '5': 0,
    '6': 1,
    '7': 0,
    '8': 2,
    '9': 1,
    'A': 1,
    'B': 2,
    'C': 0,
    'D': 1,
    'E': 0,
    'F': 0,
}


def num_closed_spaces(num_str):
    num = 0
    for c in num_str:
        num += closed_spaces[c]

    return num

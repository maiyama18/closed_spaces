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

""" try:
    file = open('log.txt', encoding='utf-8')
except FileNotFoundError:
    print('Does this show')
except PermissionError:
    print('does this show')
except Exception:
    print('does this show') """

""" try:
    with open('log.txt', 'w', encoding='utf-8') as file:
except IOError:
    print('Error when writing to file')
else:
        file.write('abcd')
        file.write('deeff')
file.close() """


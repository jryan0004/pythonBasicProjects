def names():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    i=0
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter+'u' + suffix)
        else:
            print(letter + suffix)
        

names()

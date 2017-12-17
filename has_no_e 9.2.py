def has_no_e():
    fin= open('words.txt')
    line=fin.readline()
    for line in fin:
        word = line.strip()

def print_more_than_20():
    inputfile= open('words.txt')
    for line in inputfile:
        word = line.strip()
        if len(word)>20:
            print(word)

def main():
    print_more_than_20()

main()

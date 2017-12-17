def inword(word):
    
    know=dict()
    for line in word:
        know[line]

    print(know)

def readfile():
    
    words = open('words.txt')
    new_list=[]
    know=dict()
    for line in words:
        word = line.strip()
       # new_list.append(word)
        know[word]=[word]

    print(know)


    #return new_list
    #print(word
    
    
def __main__():
    
    #inword()
    new_list=readfile()
    #inword(new_list)
__main__()

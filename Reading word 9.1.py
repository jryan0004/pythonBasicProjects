fin= open('words.txt')
line=fin.readline()

for line in fin:
    word = line.strip()
    #tword=len(word)
    if 'e' not in word:
        print(word)
        
    
    


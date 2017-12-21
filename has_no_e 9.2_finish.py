def has_no_e():
    inputfile = open('words.txt')
    writeInFile = open('has_no_e','w')
    count=0
    for line in inputfile:
        word = line.strip()
        #print(word)
        
        for letter in word:
            if letter =='e':
                count = count +1
        if count ==0:
            writeInFile.write(word)
            writeInFile.write('\n')            
            #print(word)
        else:
           count = 0    

            

def main():
    has_no_e()

main()

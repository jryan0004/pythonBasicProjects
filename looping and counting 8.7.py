def loop_count(word, l):
    count=0
    #if find is true
    v =find(word,l,count)
    for letter in word:
       
        if v >-1:
            pos=v
            count=count+1
            v =find(word,l,pos+1)
        #if letter == l:
            #count= count +1
    print(count)

def find(word,letter, index):
    
    while index <len(word):
        if word[index] == letter:
            return index
        index = index +1
        
    return -1 
loop_count('happy feet', 'p')

    

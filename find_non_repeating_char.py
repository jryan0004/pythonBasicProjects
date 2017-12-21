def find_non_repeating_char(word):
    
    i =0
    k=1
    isin =[]
    while i < len(word):
        
        while k < len(word):
            #print("first[i] =",word[i])
            if word[i]== word[k]:
                   isin.append(word[k])
                #k=1
                #print("hi",isin)
                   
            k= k+1
        i= i+1
        k=i+1
    for l in word:
        if l not in isin:
            print('the first non repeating char in ',word, 'is',l)
            return
            
    print("i =",i)
    print("k =",k)
    print(isin)
def __main__():
    word= input('please enter a word ')
    find_non_repeating_char(word)
__main__()

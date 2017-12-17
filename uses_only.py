def uses_only(word,s):
    #fin= open('words.txt')
    #line=fin.readline()
    count=0
    
    
    sizeofword = len(word)
    #if sizeofs != sizeofword:
     #   return False
    
    for l in word:
        if l  in s:
            count= count+1
            print('this is in',l)
            print(count)
                        #and i remove the and and add a whitespace to s and thats a fix but i fixed it
        elif l not in s and ' ' != l:
            #if l != ' ':
                print('this is not',l)
                return False
        
    
    #print('sw',sizeofword)    
    #print('c',count)
    #if count == sizeofword:
     #   print(l)
    return True
    #print(l)

result =uses_only('cat in the hats','acithne')#if i add a whitespace that a hack for it
#but i fixed it
print(result)

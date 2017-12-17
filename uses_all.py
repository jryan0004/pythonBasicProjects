def uses_all(word,re):
  
    #most fix this code it only work for these letter
    #sizeofword = len(word)
    #if sizeofs != sizeofword:
     #   return False
    for l in re:
     
        if l not in word: #acoutn >0 and ecoutn>0 and icoutn >0 and ocoutn >0 and ucoutn> 0:
            return False
    return True
        
    
    #print('sw',sizeofword)    
    #print('c',count)
    #if count == sizeofword:
     #   print(l)
    
    #print(l)

result =uses_all('ajhiou','aeiou')#if i add a whitespace that a hack for it
#but i fixed it
print(result)

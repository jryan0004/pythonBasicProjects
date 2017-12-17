def non_dupulicates_lette(word):
    text = list(word);
    print(text)
    i=0
    for i in range(len(text)):
        for k in text:
            print(c)
            
def has_dupulicates(word):
    d= dict()
    for c in word:
        if c not in d:
            d[c]=1
            
        else:
            d[c]+=1


    for k in d:
         if d[k]==1:
             print(k)
             
         else:
             print(k,d[k])
    
             
                 
    return d
    #count=0
    #othercount=1
    #sizeword=len(word)-1
    #while count<sizeword:
        #letter=word[count]
        #while othercount<sizeword:
            #if letter == word[othercount]:
                #return True
            #othercount= othercount+1

        #count+=1


    #return False
A='bccata'#['a','b','b','c']
non_dupulicates_lette(A)
#result=has_dupulicates(A)
#print(result)

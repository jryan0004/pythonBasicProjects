def has_dupulicates(word):
   
    count=0
    othercount=1
    sizeword=len(word)-1
    while count<sizeword:
        letter=word[count]
        while othercount<sizeword:
            if letter == word[othercount]:
                return True
            othercount= othercount+1

        count+=1


    return False
A=['a','b']
result=has_dupulicates(A)
print(result)

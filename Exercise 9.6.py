def is_abecedaria(word):
    previous = word[0]
    for l in word:
        if l<previous:
            return False
     
    return True
                
        


r=is_abecedaria('cats')
result= is_abecedaria('ab')
print(result)
print(r)

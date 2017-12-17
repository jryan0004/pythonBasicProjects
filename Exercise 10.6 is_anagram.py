def is_anagram(wordone,wordtwo):
    wordOneSize=len(wordone)
    wordTwoSize=len(wordtwo)
    if wordOneSize != wordTwoSize:
        return False
    for l in wordone:
        if l not in wordtwo:
            return False

    return True
x='cat'
b='tab'
result=is_anagram(x,b)
print(result)

def read_file():
    list_of_words = []
    fin = open('new_words.txt')
    for line in fin:
        word=line.strip()
        list_of_words.append(word)
        #print(word)
        
    
    return list_of_words
def ask_user():
    word= input('enter a word')
    list_of_words=read_file()
    print(list_of_words)
    answer=in_bisect(list_of_words,word)
    if answer != None:
        print(answer)
        print(list_of_words[answer], 'is in the list')
    else:
        print(answer)
def in_bisect(sorted_list,target):
    listSize=len(sorted_list)-1
    #print('target = ',target)
    #print('list =',sorted_list)
    left=0
    right=listSize
    if(listSize==0):
         return False
           
  
    while  left <= right:#sorted_list[mid]!= target:#left <= right:
        mid= left+(right- left)//2
       # print('this is a item in the list',sorted_list[mid])
        if sorted_list[mid] == target:
            #print('mid item =',sorted_list[mid])
            return mid
    
        elif sorted_list[mid] > target:
          #  print('>')#error <
           # print('> mid item =',sorted_list[mid])
            right= mid-1
            
            #print('index mid=',mid)
        elif sorted_list[mid] < target:
            
            left=mid+1
            #print('<')#error >
            #print('< mid item =',sorted_list[mid])
            #mid= (left+right)//2
            #print('index mid=', mid)
            
        else:
            return
ask_user()


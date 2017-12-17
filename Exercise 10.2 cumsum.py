def cumsum(t):
    listsize=len(t)-1
    i=0
    total=0
    new_list=[]
    for x in t:
    #while i<listsize:wrong
        #print('listsize =',listsize)
        #print('i =',x)
        #print('t[i] =',t[i])wrong
        total+=x#t[i+1]wrong
        #print('t[i+i] =',t[i+1)wrong
        #print('total =',total)wrong
        new_list.append(total)
       # print('total =',total) wrong
        #i=i+1 wrong
    print('list =',new_list)

t=[1,2,3]
cumsum(t)

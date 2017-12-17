def is_sorted(lis):
    listsize=len(lis)-1
    i=0
    count=0
    while i < listsize:
        if lis[i]>lis[i+1]:
            count=count+1
            #return True
        i=i+1

    if count==listsize:
        return True
    return False
t=[3,2,1]
is_right=is_sorted(t)
print(is_right)
            

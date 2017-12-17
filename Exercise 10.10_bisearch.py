def in_bisect(sorted_list,target):
    listSize=len(sorted_list)-1
    print('target = ',target)
    print('list =',sorted_list)
    left=0
    right=listSize
    if(listSize==0):
        print('There is no list that we can search')
        return False
    
    
    
    
    #print('mid index =',mid)
    while  left <= right:#sorted_list[mid]!= target:#left <= right:
        mid= left+(right- left)//2
        print('this is a item in the list',sorted_list[mid])
        if sorted_list[mid] == target:
            print('mid item =',sorted_list[mid])
            return mid
    #left
    
        elif sorted_list[mid] > target:
            print('>')#error <
            print('> mid item =',sorted_list[mid])
            right= mid-1
            #left=0
            #mid= (left+right)//2
            print('index mid=',mid)
        elif sorted_list[mid] < target:
            #right=listSize 
            left=mid+1
            print('<')#error >
            print('< mid item =',sorted_list[mid])
            #mid= (left+right)//2
            print('index mid=', mid)
            
        else:
            return
    #return mid
#a=[1,2,3,4,5,6,7,8,9]
a=['cat','cbt','cct','cdt','cet','cft','cgt']#[1,2,3,4,5,6,7,8,9]
result=in_bisect(a,'cat')
print('result=',result)
print(a[result])

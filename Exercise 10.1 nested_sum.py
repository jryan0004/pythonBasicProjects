def nested_sum(t):
    x=0
      
    
    listsize=len(t)-1
      
    total=0
    while x<listsize:
        
        total=total+sum(t[x])#gets the sum of a 2D array
        x=x+1

    print(total)
    return total
    
t=[[1,2],[3],[4,5,6]]
a=nested_sum(t)
print(a)


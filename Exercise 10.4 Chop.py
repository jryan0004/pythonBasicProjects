def middle(t):
    i=0
    sizeOft=len(t);
    new_t=t[1:sizeOft-1]
    #end_of_t=t[:sizeOft]
    #new_t.extend(end_of_t)
    print(new_t)
def chop(t):
    middle(t)
    return
a= ['1','2','3','4']
n=chop(a)
print(n)


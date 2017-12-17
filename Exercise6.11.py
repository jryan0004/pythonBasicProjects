def A(m,n):
    if(m==0):
        print('n =',n)
        return n+1
        
    if(m>0 and n==0):
        print('sm =',m)
        print('sn =',n)
        return A(m-1,1)
    if(m>0 and n>0):
        print('tm=',m)
        print('tn=',n)
        return A(m-1,A(m,n-1))
print(A(3,0))

def recurse(n,s):
    if n==0:
        print(s)
    else:
        print('thos is s=',s)
        print('thos is n=',n)
        recurse(n-1,n+s)
        
recurse(3,0)

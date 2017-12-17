def histogram(s):

    d = dict()
    for c in s:
        #if c not in d:
            d[c]=1+d.get(c,0)
            #print(d)
            #d[c] = 1
        #else:
         #   d[c] += 1
    return d
h = histogram('floccinaucinihilipilification ')
print(h)

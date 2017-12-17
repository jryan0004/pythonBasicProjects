def invert_dict(d):
    inverse = {}#dict()
    type(inverse)
    for key in d:
        val = d[key]
        print('the val',val)
        print('the key',[key])
        inverse.setdefault(val,[]).append(key)
      
    print('this is the inverse', inverse)
    return inverse
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else: d[c] += 1
    return d
#h = histogram('brontosaurus')
#inverse = invert_dict(h)
#print(inverse)
if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(d)
    for val in inverse:
        keys = inverse[val]
        print(val, keys)

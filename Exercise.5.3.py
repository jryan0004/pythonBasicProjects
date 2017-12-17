
def is_triangle(x ,y, z):
    sum=x+z
    if(sum<y):
        print('No')
    sum=y+x
    if(sum<z):
        print('No')
    sum=y+z
    if(sum<x):
        print('No')
    else:
        print('Yes')

def prompts_user():
    sideone=input('Please enter side one')
    sidetwo=input('Please enter side two')
    sidethree=input('Please enter side three')
    sideone=int(sideone)
    sidetwo=int(sidetwo)
    sidethree=int(sidethree)
    is_triangle(sideone,sidetwo,sidethree)
prompts_user()


def do_four(f,x):
    do_twice(f,x);
    do_twice(f,x);
def do_twice(f,x):
    print_cat(x);
    print_cat(x);
def print_cat(x):
    print(x);
   # print("cat");
x='csh';
do_twice(print_cat,x);

a='hello';
do_four(print_cat,a);

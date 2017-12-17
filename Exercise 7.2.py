from math import *
def eval_loop():
    line = input('Please enter a sting')
    while True:
               
        if line == 'done':
            break
        else:
            output=eval(line)
            print(output)
        line = input('Please enter a sting')    

eval_loop()

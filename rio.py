'''
Don't run this.
'''

import random

a = ['welcome', 'say hello']
b = ['spooky', 'derivative', 'vanilla']
c = ['land', 'ship', 'space', 'starstealers cooperative']

def generate():
    return a[random.randrange(len(a))] + " to " + b[random.randrange(len(b))] + " " + c[random.randrange(len(c))]

def repeat():
    oh = input("c! y/n: ")
    if oh == 'y':
        return None
    else:
        return "continue.."

if __name__ == "__main__":
    while repeat():
        print(generate())
    print("all of this, just to get: rio")
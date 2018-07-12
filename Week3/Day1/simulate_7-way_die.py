import random


def rand5():
    return random.randint(1, 5)

def rand7():
    while True:
        r = (rand5() + rand5() -1) % 7
        return r


print 'Rolling 7-sided die...'
print rand7()
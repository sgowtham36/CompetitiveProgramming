import random


def rand7():
    return random.randint(1, 7)

def rand5():
    while True:
        r = rand7()
        if r < 6:
            return r


print 'Rolling 5-sided die...'
print rand5()
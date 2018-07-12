INT_MAX = 32767

def my_function(arg):
    n = arg[0]
    k = arg[1]
    eggFloor = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(1, n+1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
    for j in range(1, k+1):
        eggFloor[1][j] = j
    for i in range(2, n+1):
        for j in range(2, k+1):
            eggFloor[i][j] = INT_MAX
            for x in range(1, j+1):
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res
    return eggFloor[n][k]

# Run your function through some test cases here
# Remember: debugging is half the battle!
print my_function([2,100])
print my_function([5,36])
print my_function([7,64])
print my_function([8,50])
print my_function([6,150])
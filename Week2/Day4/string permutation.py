def get_permutations(string):

    # Generate all permutations of the input string
    d = []
    rec(string,"",d)

    return set(d)

def rec(t, f, d):
    if len(t)==0:
        d.append(f)
        return
    for k in range(len(t)):
        rec(t[0:k]+t[k+1:],f+t[k],d)

# Tests

actual = get_permutations('')
expected = set([''])
print(actual == expected)

actual = get_permutations('a')
expected = set(['a'])
print(actual == expected)

actual = get_permutations('ab')
expected = set(['ab', 'ba'])
print(actual == expected)

actual = get_permutations('abc')
expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
print(actual == expected)
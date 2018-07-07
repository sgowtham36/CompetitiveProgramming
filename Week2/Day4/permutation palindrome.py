def has_palindrome_permutation(stri):

    # Check if any permutation of the input is a palindrome
    d = {}
    for i in stri:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    flag = 0
    for i in d:
        if d[i]%2==1:
            flag+=1

    return flag==1 or flag==0

# Tests

result = has_palindrome_permutation('aabcbcd')
expected = True
print(result == expected)

result = has_palindrome_permutation('aabccbdd')
expected = True
print(result == expected)

result = has_palindrome_permutation('aabcd')
expected = False
print(result == expected)

result = has_palindrome_permutation('aabbcd')
expected = False
print(result == expected)

result = has_palindrome_permutation('')
expected = True
print(result == expected)

result = has_palindrome_permutation('a')
expected = True
print(result == expected)
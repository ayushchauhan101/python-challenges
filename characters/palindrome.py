# # method 1
# def isPalindrome(word):
#     word = word.lower()
#     return word == word[::-1]

# method 2
def isPalindrome(word):
    word = word.lower()

    rev_word = ''.join(reversed(word))

    return word == rev_word


print(isPalindrome('AYush'))
print(isPalindrome('AAbAA'))
print(isPalindrome('aIbohPhoBiA'))
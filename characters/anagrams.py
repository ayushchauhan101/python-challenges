# check for anagrams i.e same characters different words
from collections import Counter

# # method 1
# def anagram(a,b):
#     return True if Counter(a) == Counter(b) else False

# method 2
def anagram(s:str, t:str):
    if sorted(s) == sorted(t):
        return True
    else:
        return False

print(anagram('silent', 'listen'))
print(anagram('max', 'min'))

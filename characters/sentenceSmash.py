# method 1
# def smash(words):
#     answer = ''
#     for x in words:
#         answer += x
#         answer += ' '
#     return answer.strip()

def smash(words):
    return ' '.join(words).strip()

print(smash(['  hello', 'world', 'this', 'is', 'great']))
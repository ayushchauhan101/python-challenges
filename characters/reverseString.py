# Complete the function that accepts a string parameter, and reverses each word in the string

# # method 1
# def reverse_words(text):
#     text = text.split(' ')
#     myList = (list(map(lambda x: x[::-1], text)))
#     answer = ''
#     for x in myList:
#         answer += x+' '
#     return answer.strip()


# # method 2
# def reverse_words(text):
#     return ' '.join(x[::-1] for x in text.split(' '))
#     # return ' '.join(list(x[::-1] for x in text.split(' ')))


# method 3
def reverse_words(text):
    return ' '.join(map(lambda x: x[::-1], text.split(' ')))


print(reverse_words('This is an example!'))
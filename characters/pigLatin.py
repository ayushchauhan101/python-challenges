# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# # method 1
# def pig_it(text):
#     text = text.split()

#     def magic(str):
#         if str.isalnum():
#             return str[1:] + str[0] + 'ay'
#         else:
#             return str

#     answer = list(map(magic, text))

#     result = ''
#     for x in answer:
#         result += x
#         result += ' '

#     return result.strip()


# # method 2
# def pig_it(text):
#     myList = text.split()
#     return ' '.join(x[1:]+x[0]+'ay' if x.isalpha() else x for x in myList)


# # method 3
# def pig_it(text):
#     return ' '.join(x[1:]+x[0]+'ay' if x.isalpha() else x for x in text.split())


# method 4
def pig_it(text):
    res = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)


print(pig_it('Pig latin is cool'))
print(pig_it('O tempora o mores !'))


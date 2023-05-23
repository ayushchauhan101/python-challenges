sentence = 'python is not really easy'

# print(len(sentence)) #25

# ---------------------------------
# # first letter capitalize
# print(sentence.capitalize())

# -----------------------------------
# # fills the remaining length around string with characters specified
# centeredString = sentence.center(30,'$')
# print(centeredString)
# print(sentence.center(35,'+'))


# -----------------------------------
# # count('charater',start,end)
# print(f"the number of occurence of a: {sentence.count('a')}")
# print(sentence.count('o',2,8))


# -----------------------------------
# endswith('character', start, end)
# print(sentence.endswith('easy'))
# print(sentence.endswith('not',5,13))

# returns true if mathces any of the tuple entry
# print(sentence.endswith(('difficult', 'medium', 'easy')))


# -----------------------------------
# # expandtabs
# str = 'hello\tmy name is\t ayush'
# print(str.expandtabs(8))
# print(str.expandtabs(2))


# -----------------------------------
# # find('character', start, end)
# print(sentence.find('really',10,len(sentence)))
# print(sentence[14:])


# -----------------------------------
# # format('poistional/default argument')
# print('Hi, my name is {} {}.'.format('ayush'.title(), 'chauhan'))
# print('I have {money} in my bank {act}'.format(money=7500, act='account'))


# -----------------------------------
# # index('character',start,end)
# print(sentence.index('easy'))


# -----------------------------------
# # isalnum()
# print(sentence.isalnum())
# print('asd456!'.isalnum())
# print('asd456'.isalnum())


# -----------------------------------
# .join('separator','iterable')
# text = ['this', 'is', 'a', 'string', 'into', 'list']
# print(''.join(text))
# print('\t'.join(text))
# print('---'.join(text))

# test = {'mat': 1, 'that': 2, 'cat':3}
# print('==>'.join(test))


# -----------------------------------
# .split('separator', 'max split')
print(sentence.split(' '))
print(sentence.split(' ', 2))
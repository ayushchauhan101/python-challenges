# remove empty white spaces
word = '8 j 8   mBliB8g  imjB8B8  jl  B'

def no_space(str):
    return str.replace(' ', '')

answer = no_space(word)
print(answer)
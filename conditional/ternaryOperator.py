# # def isEven(num):
# #     return 'even' if num%2==0 else 'odd'

# # print(isEven(10))

# def legalAge(age):
#     return "children" if age < 16 else "young man" if age < 50 else "old man"

# print(legalAge(20))
# print(legalAge(15))
# print(legalAge(83))


def sale_hotdogs(n):

    # if n<5:
    #     return 100*n
    # elif 10>n>=5:
    #     return 95*n
    # else:
    #     return 90*n

    # return n * (100 if n < 5 else 95 if n < 10 else 90)

    return n*100 if n<5 else n*95 if 10>n>=5 else n*90


print(sale_hotdogs(11))
print(sale_hotdogs(100))


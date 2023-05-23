# Count the number of divisors of a positive integer n

# method 1
# def divisors(n):
#     numDivs = []
#     for i in range(1,n+1):
#         if (n % i == 0):
#             numDivs.append(i)
#     return len(numDivs)


# method 2 ; count when true
def divisors(n):
    return sum(list(n%x==0 for x in range(1,n+1)))

print(divisors(12))
print(divisors(5))
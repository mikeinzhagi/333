# def jiechen(n):
#     result = n
#     for i in range(1, n):
#         result = result * i
#         n = n + 1
#     return result
#
#
# print(jiechen(100))


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(50))




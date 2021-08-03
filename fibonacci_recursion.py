def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return 'Invalid input.'
    return fib(n-1) + fib(n-2)


user = int(input('Enter number: '))
fib = fib(user)
print(fib)

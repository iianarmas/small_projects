def fact(n):
    if n == 0:
        return 1
    elif n < 0:
        return 'Invalid input.'
    return n * fact(n - 1)


user = int(input('Enter number: '))
factorial = fact(user)
print(factorial)

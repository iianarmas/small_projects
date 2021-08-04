def digital(n):

    if n >= 0:
        n = [i for i in str(n)]
        n = [int(i) for i in n]

        if len(n) > 1:
            return digital(sum(n))
        return n[0]
    return 'Invalid input'


user = int(input('Enter number: '))

d_root = digital(user)

print(f'Digital Root is: {d_root}')

# can also be written as
def digital(n):
    return n % 9 or n and 9

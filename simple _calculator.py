def calculate(values):

    if values[1] == '+':
        return sum(int(i) for i in values if i.isdigit())
    elif values[1] == '-':
        return int(values[0]) - int(values[2])
    elif values[1] == '*':
        return int(values[0]) * int(values[2])
    elif values[1] == '/':
        return int(values[0]) / int(values[2])
    else:
        return f'Cannot compute expression: {values}'


print('(Please use spaces to separate each value.)')
user = input('Enter expression: ').lower().strip().split()

print(calculate(user))


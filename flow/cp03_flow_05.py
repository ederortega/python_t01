# Apply basic operations (+, -, *, /) with for loop
operations = ['a', 'm', 'x', 'd', 5]
operand_1 = 11
operand_2 = 3
result = 0

for op in operations:
    if op == 'a':
        result = operand_1 + operand_2
        print('{} + {} = {}'.format(operand_1, operand_2, result))
    elif op == 'm':
        result = operand_1 - operand_2
        print('{} - {} = {}'.format(operand_1, operand_2, result))
    elif op == 'x':
        result = operand_1 * operand_2
        print('{} * {} = {}'.format(operand_1, operand_2, result))
    elif op == 'd':
        result = operand_1 / operand_2
        print('{} / {} = {}'.format(operand_1, operand_2, result))

# operations and values
operations = [('a', 5, 3), ('m', 8, 6), ('x', 12, 5), ('d', 18, 3)]

for op, operand_1, operand_2 in operations:
    if op == 'a':
        result = operand_1 + operand_2
        print('{} + {} = {}'.format(operand_1, operand_2, result))
    elif op == 'm':
        result = operand_1 - operand_2
        print('{} - {} = {}'.format(operand_1, operand_2, result))
    elif op == 'x':
        result = operand_1 * operand_2
        print('{} * {} = {}'.format(operand_1, operand_2, result))
    elif op == 'd':
        result = operand_1 / operand_2
        print('{} / {} = {}'.format(operand_1, operand_2, result))

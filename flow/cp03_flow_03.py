# Apply basic operations (+, -, *, /)
operations = ['a', 'm', 'x', 'd']
operand_1 = 25
operand_2 = 3
result = 0

op = 'a'
if op in operations:
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

    # check result data type

else:
    print('Operation not allowed.')

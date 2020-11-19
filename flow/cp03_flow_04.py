# fill even numbers
even_numbers = []
upper_value = 15
for x in range(upper_value):
    if x % 2 == 0:
        even_numbers.append(x)

print('Even numbers: {}'.format(even_numbers))

# set
first_set = {'Mario', 'Luigi', 'Kupa'}

second_set = {'Princesa', 'Kupa'}

# print union
print(' UNION '.center(70))
print(first_set.union(second_set))

# print intersection
print(' INTERSECTION '.center(70, '-'))
print(first_set.intersection(second_set))

# try to add existing value
print(' NO DUPLICATE VALUES '.center(70, '-'))
first_set.add('Kupa')
print(first_set)

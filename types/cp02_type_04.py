# dict
first_dict = {
    'name': 'Jon',
    'last-name': 'Snow',
    'age': 38
}

# print type
print(type(first_dict))

# access key
print(first_dict['name'])

# add key
first_dict['profesion'] = 'Ingeniero'

# update dict
first_dict['profesion'] = 'Doctor'

del first_dict['age']
print(first_dict)

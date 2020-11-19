str_names = 'Neo,Smith,Morfeo,Trinity,Naiobi'
index = 0
names = str_names.split(',')
print(names)
while(index < len(names)):
    if len(names[index]) <= 5 or names[index] == 'Trinity':
        print(names[index].upper())

    index += 1

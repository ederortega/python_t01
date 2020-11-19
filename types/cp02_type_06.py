# bool and bytes
true_value = True
false_value = False

# bytes
x = bytes(4)
print(x)

x = b'Camar\xc3\xb3n que se duerme'
print(x)
print(x.decode())

x = bytes('Camarón que se duerme', 'utf8')
print(x)

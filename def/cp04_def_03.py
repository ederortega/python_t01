# passing arguments
# - It's just assigning an object to a local variable
# - Caller it's not affected unless a mutable object (parameter) is modified
def square(x):
    print('Square = {}'.format(x * x))


def cube(x):
    x = x ** 3
    print('Cube = {}'.format(x))

"""
def square_list(x_list):
    for i, x in enumerate(x_list):
        x_list[i] = x * x
"""

if __name__ == "__main__":
    a = 7
    # a_list = [1, 2, 3]
    square(a)
    cube(a)
    # square_list(a_list)
    print('Original value = {}'.format(a))
    # print('Modified list = {}'.format(a_list))

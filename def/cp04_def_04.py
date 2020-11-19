# Positional arguments
# Keyword arguments
# default values
def func_with_positional(x, y, c):
    z = x * x + 2 * y + c
    print('F(z) = {}'.format(z))


def func_with_default(x, y, c=0):
    z = x * x + 2 * y + c
    print('F(z) = {}'.format(z))


if __name__ == "__main__":
    # positional
    func_with_positional(2, 7, 0)




    # by keyword
    # func_with_positional(c=0, x=3, y=5)
    
    
    
    
    
    
    # with default
    # func_with_default(2, 7)

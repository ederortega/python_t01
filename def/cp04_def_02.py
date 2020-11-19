# variable scope
def custom_function():
    scope = 10
    print('Function scope value is ({})'.format(scope))
    # inner function


if __name__ == "__main__":
    scope = 7
    print('Global scope value is ({})'.format(scope))
    custom_function()

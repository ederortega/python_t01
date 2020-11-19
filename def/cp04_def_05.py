# variable positional arguments
def func_with_variable_args(*args):
    print('Sum(z) = {}'.format(sum(args)))


# variable keyword arguments


if __name__ == "__main__":
    # positional
    func_with_variable_args(2, 7, 3)
    # unpack variables

    # keyword arguments
# *args
# In cases when we don't know how many arguments will be passed
# to a function, like when we want to pass a list or a tuple of values,
# we use *args


def func(*args):
    for i in args:
        print(i)

func(3,2,1,4,7)


# **kwargs takes keyword arguments when we don't know
# how many there will be


def func(**kwargs):
    for i in kwargs:
        print(i, kwargs[i])

func(a=1, b=2, c=7)


# The words args and kwargs are a convention, and we can use anything in their place.
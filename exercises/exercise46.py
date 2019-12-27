# I could not solve this exercise.
# Using generator and class, iterable objects and iterator
# These are the terms that I am not getting the concepts with.
# Googling through those terms but not many people can provide clear
# Explanations on those. In this exercise, I decided to revise generator and put it in this python file.



# Generator functions are a special kind of function that return a lazy iterator.
# These are objects that you can loop over like a list.
# However, unlike lists, lazy iterators do not store their contents in memory.


# Today, I am getting a few examples of generator in order to gain understandings
# on generator.


def first(n):
    num = 0

    while num < n:
        if num % 7 == 0:
            yield num
        num += 1


first(10)


def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row



# Generating an Infinite Sequence

def infinite_sequence();
    num = 0
    while True:
        yield num
        num = num + 1









# def firstn(n):
#     num, nums = 0, []
#     while nums < n:
#         nums.append(num)
#         num = num + 1
#     return nums
#
#
# class GeneratorIterable:
#     def __init__(self, number):
#         self.number = number
#         self.counter = 0
#         self.number_list = []




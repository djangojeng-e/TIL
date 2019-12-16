import os 
# cur_directory = print(getcwd())     # Return the current working directory 
# # print(cur_directory)
# print(os.chdir) # Change current working directory 

# os.system('mkdir today')    # Run the command mkdir in the system shell. 

# There was today folder created in the root folder. 

# print(dir(os))      # returns a list of all module functions. 

# print(help(os))     # returns an extensive manual page crated from the module's docstring/


# import shutil 
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')


# import glob
# file_list = glob.glob('*.py')
# print(file_list)



# import sys 
# print(sys.argv)

# # The argparse module provides more sophiscated mechanisms to process command line arguments

# import argparse

# parser = argparse.ArgumentParser(prog = 'top', description = 'Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)


import re
# f_words = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# print(f_words)

# sub = re.sub(r'\(\b[a-z]+) \1', r'\1', 'cat in the hat')
# print(sub)


a = 'tea for too'.replace('too', 'two')
print(a)

# Mathematics 

import math 
cos = math.cos(math.pi / 4)
print(cos)

log = math.log(1024, 2)
print(log)


# Random module provides tools for making random selections. 


# import random 
# fruit = random.choice(['apple', 'pear', 'banana'])
# print(fruit)

# sample = random.sample(range(100), 10) # sampling without replacement 

# print(sample)

# random_float = random.random()
# print(random_float)

# integer_number = random.randrange(6)     # random integer chosen from range(6)
# print(integer_number)




# The statistics modue calculates basic statistical properties 
# (the mean, median, variance, etc) of numeric data. 

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print("mean", statistics.mean(data))
print("median :", statistics.median(data))
print("variance :", statistics.variance(data))

#
# from urllib.request import urlopen
# with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
#     for line in response:
#         line = line.decode('utf-8')     # Decoding the binary data to text.
#         if 'EST' in line or 'EDT' in line:  # Look for Eastern Time
#             print(line)
#
# import smtplib
#
# server = smplib.SMTP('localhost')
# server.sendmail('soothsayer@exmple.org', 'jcaesar@exmple.org',
#                 """To : jcaesar@example.org
#                    From : soothsayer@example.org
#
#                    Beware the Ideas of March.
#                    """)
# server.quit()
#
# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))
#
# t = zlib.compress(s)
# print(len(t))
#
# u = zlib.decompress(t)
# print(u)
#
# print(zlib.crc32(s))

from timeit import Timer

a = Timer('t=a; a=b; b=t', 'a=1;b=2').timeit()
print(a)
b = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(b)

#
#
# def for_number(number):
#     for_list = []
#     for i in range(0, 2000000):
#         for_list.append(i)
#
# def while_number(number):
#     while_list = []
#     i = 0
#     while i < 2000000:
#         while_list.append(i)
#         i = i + 1
#
# d = Timer(while_number(2000000)).timeit()
#
# print(d)
#
# c = Timer(for_number(2000000)).timeit()
# print(c)

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0


    """
    return sum(values) / len(values)

import doctest

z = doctest.testmod()
print(z)


import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20,30,70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises((ZeroDivisionError)):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()
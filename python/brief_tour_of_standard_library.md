# Standard Library 



Python offers basic standard Library to be used by the programmer. The documentation tutorial introduces  Standard library in Chapter 10. 





# Operating System Interface 



**The os module provides functions for interacting with the operating system**





```python
import os 
# cur_directory = print(getcwd())     # Return the current working directory 
# print(cur_directory)
print(os.chdir) # Change current working directory 

os.system('mkdir today')    # Run the command mkdir in the system shell. 

# There was today folder created in the root folder. 


```



**import os** 

Careful not to use from os import * as this command will keep os.open() 



**use of dir() and help() functions for aids on working with large modules like os:**





```python

print(dir(os))      # returns a list of all module functions. 

print(help(os))     # returns an extensive manual page crated from the module's docstring/


```





**shutil provides a higher level interface that is easier to use. **



```python


import shutil 
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')


```





**Glob module provides a function for making file lists from directory wildcard searches.**





```python
import glob

glob.glob('*.py')



```





**Command Line Arguments **



Common utility scripts often need to process command line arguments. These arguments are stored in the sys module's argv attribute as a list. 



```python


import sys 
print(sys.argv)

# The argparse module provides more sophiscated mechanisms to process command line arguments

import argparse

parser = argparse.ArgumentParser(prog = 'top', description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)



```



**Error Output Redirection and Program Termination **



**sys module also has attributes for stdin, stdout and stderr.**



```python
sys.stderr.write('warning, log file not found starting a new one \n')
```





**String Pattern Matching **



The re module provides regular expression tools for advanced string processing. Regular expression takes a great role when matching up complicated characters and strings. It is used for complex matching and manipulation. 



```python
import re 

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# finds words starting with f 

re.sub(r'\b[a-z]+ \1', r'\1', 'cat in the hat')

a = 'tea for too'.replace('too', 'two')
print(a)
```





## Mathematics 



The math module gives access to the underlying C library functions for floating point math. 



```python
import math 
cos = math.cos(math.pi / 4)
print(cos)

log = math.log(1024, 2)
print(log)
```





# Random module 







```python


# Random module provides tools for making random selections. 


import random 
fruit = random.choice(['apple', 'pear', 'banana'])
print(fruit)

sample = random.sample(range(100), 10) # sampling without replacement 

print(sample)

random_float = random.random()
print(random_float)

integer_number = random.randrange(6)     # random integer chosen from range(6)
print(integer_number)
```





# Statistics 



```python
# The statistics modue calculates basic statistical properties 
# (the mean, median, variance, etc) of numeric data. 

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))
```





# Internet Access





There are a number of modules for accessing the internet and processing internet protocols. Two representative modules would be **urllib.request** and **smtplib**



```python
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)



import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()
```



The example requires a mailserver running on localhost though. 





# Dates and Times 





The **datetime** module supplies classes for manipulating dates and times in simple or complex ways. 

Dates can be easily constructed and formatted. 



Use Jupyter notebook to test this. 



```python
# %m = month 
# %a = day in number 
# %y = year in number (short form only 2 digits)
# %b = Month in Word (e.g. December -> Dec)
# %Y = Year in number (Full format e.g. 2019)
# %A = Day of the week (e.g. Monday)
```




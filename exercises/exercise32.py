import math


def square_root():
    c = 50
    h = 30
    D = []
    for i in range(0, 3):
        numbers = int(input("Please enter your number"))
        if numbers not in D:
            D.append(numbers)
    print(D)
    Q = [round(math.sqrt(2 * c * number / h)) for number in D]
    print(Q)


square_root()


# below is the solution from author. However, the answer does not seem to
# meet up with the question exactly.


c = 50
h = 30
value = []
items = [x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))





def numbers(n):
    for number in range(0, n + 1):
        if number % 5 == 0 and number % 7 == 0:
            yield number

n = int(input("Please enter your number"))

values = []
for i in numbers(n):
    values.append(str(i))

print(",".join(values))


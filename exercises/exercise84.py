number = int(input("Please enter your number"))
def generator(n):
    for num in range(0, n+1):
        if num % 2 == 0:
            yield num

generated_number = generator(number)

values = []
for i in generated_number:
    values.append(str(i))

print(",".join(values))

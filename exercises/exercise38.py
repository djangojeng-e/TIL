
numbers = []
for number in range(1000, 3001):
    numbers.append(number)

even_digit_numbers = []

for nums in numbers:
    num = str(nums)
    even_digit = []
    for digit in num:
        if int(digit) % 2 == 0:
            even_digit.append(str(digit))
            if len(even_digit) == 4:
                even_digit_numbers.append("".join(even_digit))
            else: continue
        else:
            continue

print(",".join(even_digit_numbers))

# Official Solution indicates.. as below.

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 ==0) and (int(s[1]) % 2 ==0) and (int(s[2]) % 2 ==0) and (int(s[3]) % 2 ==0):
        values.append(s)

print(",".join(values))
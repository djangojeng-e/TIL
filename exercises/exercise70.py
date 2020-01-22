
number_list = [x for x in range(1, 21)]

squarenumbers = map(lambda x: x ** 2, number_list)

# squarenumbers is created as object via lambda x: x ** 2
# list(squarenumbers) will return a list of object created by lambda.

print(list(squarenumbers))
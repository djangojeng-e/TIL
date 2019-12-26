from operator import itemgetter

tuples = []
for i in range(0, 4):
    name = input("Please enter your name : ")
    age = input("Please enter your age : ")
    score = input("Please enter your score : ")
    tuple = (name, age, score)
    tuples.append(tuple)

print(tuples)

print(sorted(tuples, key=itemgetter(0,1,2)))
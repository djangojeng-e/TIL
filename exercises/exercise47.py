import math


# Before moving on to the solution, we need to make assumptions that
# Robot's original coordinate is (0, 0)
# There are two axis x-axis and y-axis (represent horizontal and vertical algins respectively)
# The distance between two points is caluclated using the following formula.
# distance = square root of (x ^ 2 + y ^ 2)


up = int(input("Please enter the number for the move to up : "))
down = int(input("Please enter the number for the move to down : "))
left = int(input("Please enter the number for the move to left : "))
right = int(input("Please enter the number fo the move to right : "))

print(f'UP : {up}\nDOWN : {down}\nLEFT : {left}\nRIGHT : {right}')

horizontal_move = abs(right - left)
vertical_move = abs(up - down)

distance = math.sqrt((horizontal_move**2 + vertical_move**2))


print("The distance is : ", int(distance))
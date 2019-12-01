horizontal_border = "---"
vertical_border = "|"

def boxes(i):
    for line in range(i):
        print((" " + horizontal_border) * i)
        print((vertical_border + "\t") * (i + 1))

    print((" " + horizontal_border) * i)        # Closing the box.

boxes(8)
# Why do we need the __init__() function in classes?
# What else helps?


# __init__() is what we need to initialize a class when we initiate it.


class Orange:
    def __init__(self):
        self.color = 'orange'
        self.type = 'citrus'

    def setsize(self, size):
        self.size = size

    def show(self):
        print(f"color: {self.color}, type: {self.type}, size: {self.size}")

o = Orange()
o.setsize(7)
o.show()

# An orange has been already classified as orange and type is being citrus
# The only value needed to be set was the size which was entered as 7
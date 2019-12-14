#
# class String(self, string):
#     pass
#
#     def getstring(self):
#         string = input("Please input your string.")
#
#     def printstring(self):
#         string = self.string.upper()
#         print(string)
#
#

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter your string.")

    def printString(self):
        print(self.s.upper())

stringobject = InputOutString()
stringobject.getString()
stringobject.printString()




# Write a program to enter a string and the print it in uppercase
class InputOutputstring(object):

    def __init__(self):
        self.str =""
    def inputstring(self):
        self.str= input("Enter a string withon double quotes:")
    def outputstring(self):
        print self.str.replace("yes", "no")

obj = InputOutputstring()
obj.inputstring()
obj.outputstring()
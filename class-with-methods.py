class string(object):
    def __init__(self):
        self.st = ''

    def getString(self):
        """Get string from console."""
        self.st = raw_input()


    def printString(self):
        """Print the string in uppercase"""
        print self.st.upper()


strObj = string()
strObj.getString()
strObj.printString()

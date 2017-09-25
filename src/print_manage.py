# Printer functions come here

import re

class PrintManager():
    def __init__(self):
        self.__printComp = re.compile("^print |^write ")
        # printing things like "string a" and "string b"
        # (notice the and keyword) don't work

    def decode(self, msg):
        # instead of being treated as a string,
        # msg should be treated as a series of arguments
        msg = re.sub(self.__printComp, "", msg)

        # returns the message to be printed
        return msg


if __name__ == "__main__":
    dummy = PrintManager()
    print dummy.decode("print 5,'Hello'")


# The assignation "manager" is here
# Here, the assignation parameters are processed and the type of operation is detected ( simple, addition, subtraction, multiplication, division)
# It is supposed that the "central manager" already detected that we are doing an assignation (even though the first parameter will still be "let")
# Examples: let x be 5
#           let avc be "Hello World"
#           let av = 5
#           let xyz be 5 multiplied by 4 divided by 2.4
#                           added to 10 subtracted with 40

import re

class AssignationManager():
    def __init__(self):
        # only spaces are supported right now
        # maybe add support for whole \s
        self.__letComp = re.compile("^let ")
        self.__eqComp = re.compile(" be | is | equals ")
        self.__mulComp = re.compile(" multiplied by | [xX] ")
        self.__divComp = re.compile(" divided by ")
        self.__addComp = re.compile(" added to | plus ")
        self.__subComp = re.compile(" subtracted with | minus ")

    def decode(self, msg):
        msg = re.sub(self.__letComp, "", msg)
        msg = re.sub(self.__eqComp, " = ", msg)
        msg = re.sub(self.__mulComp, " * ", msg)
        msg = re.sub(self.__divComp, " / ", msg)
        msg = re.sub(self.__addComp, " + ", msg)
        msg = re.sub(self.__subComp, " - ", msg)

        return msg


if __name__ == "__main__":
    dummy = AssignationManager()
    result = dummy.decode("let xyz be 5")
    print result


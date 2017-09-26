# Here, we take the list of commands
# and try to guess which type it is,
# plus try to execute it

import re

from assign_manage import AssignationManager
from print_manage import PrintManager

class MainManager():
    def __init__(self):
        self.assigner = AssignationManager()
        self.printer = PrintManager()
        self.__assignComp = re.compile("^let ")
        self.__printComp = re.compile("^print |^write ")
        self.__variables = {}

    def _isAssignation(self, comm):
        found = re.search(self.__assignComp, comm)
        return (found is not None)

    def _isPrint(self, comm):
        found = re.search(self.__printComp, comm)
        return (found is not None)

    def decode(self, msg):
        # This time, msg is a list of strings
        # each one representing a different command

        for each in msg:
            # first, identify the type of the command
            if self._isAssignation(each):
                result, value = self.assigner.decode(each)
                print result, "=", eval(value)
                self.__variables[result] = eval(value)
            elif self._isPrint(each):
                result = self.printer.decode(each)
                print result

    def _print_variable_dict(self):
        for key in self.__variables.keys():
            print key, ":", self.__variables[key]


if __name__ == "__main__":
    dummy = MainManager()
    tasks = [
            "let x be 20",
            "let y be 5 multiplied by 6",
            "let a be \"Hello, Carl\"",
            "print 20, \'Sunshine\'"
        ]
    dummy.decode(tasks)
    print "\nKeys and their values:"
    dummy._print_variable_dict()


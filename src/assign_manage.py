# The assignation "manager" is here
# Here, the assignation parameters are processed and the type of operation is detected ( simple, addition, subtraction, multiplication, division)
# It is supposed that the "central manager" already detected that we are doing an assignation (even though the first parameter will still be "let")
# Examples: let x be 5
#           let avc be "Hello World"
#           let av = 5

class AssignationManager():
    def __init__(self, params):
        self.keyword = None
        self.result = None
        self.operands = []
        self.operator = None
        self.params = params

    def print_debug(self):
        print "Keyword:", self.keyword
        print "Result:", self.result
        print "Operands:", self.operands
        print "Operator:", self.operator
        self.print_operation()

    def print_operation(self):
        print self.result, "=", self.operands[0]
        for operand in self.operands[1:-1]:
            print self.operator, operand
        if len(self.operands) > 1:
            print self.operands[-1]
        
        # it is not really correct, but it will do for now

    def decode(self):
        # the first parameters must be "let"
        self.keyword = self.params[0]

        # then, the next parameter should be the result
        self.result = self.params[1]

        # then, the 3rd parameter should be "be" or =
        self.operator = self.params[2]
        if self.operator in ("be"):
            self.operator = "="

        # the rest must be processed, as it might be an expression
        # right now, let's suppose it is just an operand (eg 5 or "Hello World")
        self.operands.extend(self.params[3:])


if __name__ == "__main__":
    dummy = AssignationManager("let x be 5".split())
    dummy.decode()
    dummy.print_debug()


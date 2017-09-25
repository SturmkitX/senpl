# Sanity checks

from assign_manage import AssignationManager

assign_tests = {
        "let x be 5 multiplied by 20" : "x = 5 * 20"
        }

assigner = AssignationManager()
for each in assign_tests.keys():
    print "Testing assignation \"", each, "\" ... ",
    result = assigner.decode(each)
    if result == assign_tests[each]:
        print "OK"
    else:
        print "FAIL"


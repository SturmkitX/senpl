# Sanity checks

from assign_manage import AssignationManager

rez = {
        "let x be 5 multiplied by 20" : "x = 5 * 20"
        }

assigner = AssignationManager()
for each in rez.keys():
    print "Testing assignation \"", each, "\" ... "
    result = assigner.decode(each)
    if result == rez[each]:
        print "OK"
    else:
        print "FAIL"


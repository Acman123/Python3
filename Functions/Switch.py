#My attempts at making a switch statement (as found in C++) in Python3.

def switch(case, *args):
    if not isinstance(args[0],str):
        args = list(*args)
    try:
        case = int(case)
        return args[case -1]
    except (IndexError, TypeError):
        case = input("Invalid input for case. Try again.\n")
        return switch(case,*args)

def advancedSwitch(case,expressions,results):
    newExpressions = [str(case) + ' ' + i for i in expressions]
    evaluation  = [eval(i) for i in newExpressions]
    return results[evaluation.index(True)]

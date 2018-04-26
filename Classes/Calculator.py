from math import *

class Calculator():
    def listVars(self):
        variables = str(self.__dict__).replace("{","").replace("}","").split(', ')
        for i in variables:
            print(i)
    
    def calc(self):
        while True:
            promptEq = "Enter your equation, enter 'list' to list your stored variable, or enter 'Q' to quit."
            responseEq = input(promptEq + "\n")
            if responseEq in ['Q','q']:
                print()
                break

            elif responseEq == 'list':
                print()
                self.listVars()
                print()
                continue

            for i in list(self.__dict__.keys()):
                execPhrase1 = str(i) + "= self." + str(i)
                exec(execPhrase1)
                
            try:
                result = eval(responseEq.replace("^","**"))
            except:
                print("Invalid equation:",responseEq, "\nTry Again.\n")
                calc()

            print("Result:", result)

            promptMem = "\nDo you want to store this result? (Y/N)"
            responseMem = input(promptMem + '\n').title()
            if responseMem == "Y":
                promptVar = "\nWhat variable would you like to store it on?"
                responseVar = input(promptVar + '\n')
                execPhrase2 = 'self.' + responseVar + '=' + str(result)
                exec(execPhrase2)
                
            print()

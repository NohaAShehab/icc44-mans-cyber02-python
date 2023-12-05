print("---------------- welcome to inputs module ---------------- ")

def askforInt(message='Please enter number'):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("----- please enter valid number ------")




def askforString(message='Please enter string'):
    while True:
        inputstr = input(message)
        if inputstr.isalpha():
            return inputstr
        print("---- not valid string ----")


""" I need these lines to be run when only execute this file"""

if __name__=='__main__':
    print("--- this code will run only if you start the run from inputsmodule")
    print(askforInt("please enter age "))
    print(askforString())


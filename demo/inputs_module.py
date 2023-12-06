import  time

""" 1- function continue asking user to
enter string until he enters valid string (not empty, consists only from chars)"""

def askforstring(message='please enter a string'):
    while True:
        inputstring  = input(message)
        if inputstring.isalpha():
            return inputstring

        print("---- please enter valid string ----")



def askforInt(message='please enter a number: '):
    while True:
        inputnumber = input(message)
        if inputnumber.isdigit():
            return int(inputnumber)

        print("---- please enter valid number number ")



def generate_id():
    id = round(time.time())
    # print(id)
    return id



if __name__ == '__main__':
    # print(askforstring("please enter name : "))
    # print(askforInt('please enter age: '))

    generate_id()
    pass

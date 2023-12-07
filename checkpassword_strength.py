# import modules/package builtin/installed
import base64
from getpass import getpass
import maskpass
import  re

# import userdefined modules

# def check_password_strength(password):
#     """ password pattern """
#     pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
#     res = re.match(pattern, password)
#     if re:
#         print("----- valid password -----")
#         return True
#
#     return False


def askforpassword(message='please enter password: '):

    """ password pattern """
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    while True:
        password = input(message)
        res = re.match(pattern, password)
        if res:
            print("----- valid password -----")
            return True

        print("please choose more complex password ")

""" hide password """
def ask_password_hidden():
    password = getpass()  # when you run application using python3 script.py--> notice the change
    print(f" enterned password is {password}")

def use_mask_password():
    pwd = maskpass.askpass()
    # pwd = maskpass.askpass(prompt="please your password", mask='$')
    print(f"-=== password = {pwd}")
    """ encoding password  """
    password__ = pwd.encode("UTF-8")
    print(f"password = {password__}")
    """ base64 password   """
    encpwd = base64.b64encode(pwd.encode("utf-8"))
    print(f" encrypted passed: {encpwd}")



if __name__ == '__main__':
    # print(askforpassword("please enter your new password: "))
    # ask_password_hidden()
    use_mask_password()
    pass

# import  math
# print(math.pi)
# print(math.e)
# print(math.cos(1.5))
# print(math.sin(1.5))
""" os """
# import  os  # operating system
#
# print("##",os.getcwd())  # pwd
#
# print(os.name)
# print(os.getlogin())
#
# os.system('ls -l')
#
# # os.system('mkdir mmm')
#
# # os.rmdir('mmm')
#
# os.system('ip addr show')

""" re  --->regular expressions  """


# email  = ''
#
# ipversion4= ''

import  re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email = input("please enter your email address: ")

# res=re.match(regex, email)
# print(res)
#
#
# if res:
#     print("--- correct email ---")
# else:
#     print("--- invalid email -----")


""" match function return True if first part of the string follows pattern"""


# fullmatch function return match object if all the string follow pattern
res=re.fullmatch(regex, email)
print(res)


if res:
    print("--- correct email ---")
else:
    print("--- invalid email -----")



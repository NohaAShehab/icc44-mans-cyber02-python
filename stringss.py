
"1- define string "
name= 'information technology institute'
email = ''

"2- get len of string"

print(len(name))

"3- access string parts using index --> start from 0 "

print(name[2])
""" 4- slicing the string """
print(name[2:])

print(name[3:8])

print(name[:10])

print(name[::])
print(name[::-1])
print(name[::3])

"""5- get count of char in the string """
print(name.count('i'))

"""6- get index of the char in the string """
print(name.index('i'))  # get index of the first occurrence of the element .

""" 7- string is immutable datata type ===> """

# name[10]='#'  # TypeError: 'str' object does not support item assignment


"""8-some operations on the string always returns with new String """

"""1- string concatenation """

fname = 'noha'
midname = 'abdelhady'
lname= 'Shehab'


# fullname= fname + midname + midname + lname
# print(fullname)

"""2- string interpolation"""
fullname= fname  + midname  * 2 + lname  # fullname is new string
print(fullname)


"""3- formating the string """
no_of_students = 25
track = 'cybersecurity'

# info =  'we have {0} students in {1} track'
# print(info)
# print(info.format(no_of_students, track))   # new string
# print(info.format(100 , 'Ai'))
# print(info.format(track, no_of_students))

info =  'we have {abbasss} students in {mytrack} track'
print(info)

# format function with keyword arguments
print(info.format(mytrack=track, abbasss=no_of_students))   # new string

"""f-format string  ---> depends exisiting variables  in memory"""
name = 'noha'
work = 'iti'
data = f'My name is {name}, I works at {work}'
print(data)


"""replacing part of the string """
msg = 'we support hamas  a a a a a aa a a  '  #replace a , with @

print(msg.replace('a', '@', 2))


""" formating your string with these function """

work = 'information technology institute'

print(work.upper())
print(work.lower())
print(work.title())
print(work.capitalize())


""" examine string content """
name = 'noha '
print(name.islower())
print(name.isupper())
print(name.isalpha())  # return True only if string consists of alphas a-z
print(name.isdigit())  # return True only if string consists of digits 0-9
num = '100'
print(num.isdigit())

""" ask user to enter string """
# name = input("please enter your name: ")  # return string always
#
# print(name, type(name))

""" check this calculator """

"""Never Ever Do something like this """
# num1 = int(input("please enter first number: "))
# num2 = int(input("please enter second number: "))
# res = num1 + num2
# print(f"res = {res}")

""" check this """
# num1 = input("please enter first number: ")
# num2 = input("please enter second number: ")
# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
#     res = num1 +num2
#     print(res)
# else:
#     print("---num1 , num2 must be integers ")



""" strip string  """
message = '        we support hamas                     '
print(len(message))
""" strip whitespaces and tabs  from the beginning and end of string """
print(message.strip())  # new string

print(message.lstrip())
print(message.rstrip())

""" strip specific char from the string """

message = '#                      we support hamas                '
print(message.strip('#'))
print(message.strip('#w '))
print(message.lstrip('#w '))


### for loop
# name =' iti '
# count = 0
# for char in name:
#     # print(char, name.index(char))
#     print(char, count)
#     count +=1



# enmurate function ?

enum_name = enumerate("iti")
print(enum_name)  # generate index for each char

for index,char in enum_name:
    print(f"{index}: {char}")



""" check if char exists in the string """
print("n" in "noha")

print("o" in "aeiou")








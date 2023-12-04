""" functions with known number of arguments """
"""
    functions ?
    special variable --> refers to code --> accomplish specific task

    write once ---> use it many times

"""

"1- define a function"

# def myfunc():
#     pass
#
#
# res = myfunc()  # call the function
# print(res)  # None

"function "

# def myfunc():
#     return
#
#
# res = myfunc()  # call the function
# print(res)  # None

""" function do somthing """

# def helloHamas():
#     print("Hello Hamas --->Allah with you ")
#
# r=helloHamas() # calling
# print(r)


"""function return with data """

# def ask_for_fullname():
#     fname=input("Enter your first name: ")
#     lname=input("Enter your last name: ")
#     fullname=f"{fname} {lname}"
#     print(fullname)
#     return fullname.upper()
#
# res=ask_for_fullname()
# print(res)
#


""" function accept data , and return with data ? """
# def sum_numbers(num1 , num2 ):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#     return res
#
# r = sum_numbers(3,4)
# print(r)


""" check this """
# def sum_numbers(num1 , num2 ):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#     return res

# r = sum_numbers("3","4")
# print(r)
# r = sum_numbers("3",5)  #TypeError: can only concatenate str (not "int") to str
# print(r)

""" --- solve the problem"""
# def sum_numbers(num1 , num2 ):
#     print(type(num1), type(num2))
#     if num1.isdigit() and num2.isdigit():
#         print(f"num1={num1}, num2={num2}")
#         res = int(num1) + int(num2)
#         print(res)
#         return res
#
# # r= sum_numbers(34,5)
# r = sum_numbers("33",'333')

""" ?????? """
# def sum_numbers(num1 : int , num2:int ):  # readable code
#     print(type(num1), type(num2))
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#     return res
#
# # r= sum_numbers(34,5)
# r = sum_numbers("33",'333')

""" python is loosely dynamically typed lang detect varaible type in runtime"""

""" you slove the problem on your own ? """

## confirmation on type after input
#
# print(isinstance(10 , int))
#
# print(isinstance('iti', str ))
#
# print(isinstance('100', int ))
#
#
# def sum_numbers(num1 , num2 ):
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         print(res)
#         return res
#     else:
#         print("---------- num1 and num2 must be integers --------")
#
# # r= sum_numbers(34,5)
# r = sum_numbers("33",'333')
#
# mm = sum_numbers(4,5)
# print(mm)

""" check this """

def sumnum(num1,num2):
    res = num1 + num2
    print(res)

# sumnum(4) #TypeError: sumnum() missing 1 required positional argument: 'num2'

" functions with default arguments ? "

# def sumnum1(num1, num2=10):
#     print(f"num1={num1}, num2={num2}")
#     res = num1 + num2
#     print(res)
#
# sumnum1(4)
# sumnum1(4,5)
#
# print(3,5,6,7,7, sep='||')
#
# print("noha", end='#')
# print("shehab")
#


""" function with unknown number of  arguments ? """

# print()
# print(3)
# print("iti", 44,'33', 455)
#
# def ask_for_candidates(*candidates):  # arguments variable can be zero or more
#     print(candidates)
#
# ask_for_candidates()
# ask_for_candidates("ahmed")
# ask_for_candidates("Ahmed", 'ali', 'mohamed', 'ali')

"""  """

def introduce_your_self(**info):  # keyword argument
    print(info)

introduce_your_self()
introduce_your_self(fname='ahmed')
introduce_your_self(name='ahmed ali', city='cairo')
introduce_your_self(lname='test', age=10)




tem= 'we have {noofstudents} students'
print(tem.format(noofstudents='10'))


"""
    3 
    1
    2  --> 2*1 , 2*2
    3
    [[1],[2,4], [3,6.9]]
    

    4
    [[1], [2,4], [3,6,9], [4,8,12,16]]
    
    noha >> ahon
    
    'abdulrahmanosuz'
    abdu
    lr
    ahm
    anosuz  # this is the longest substring 
    
    am
    pm
    
    [apple, banana, cherry]
    noha
    -----
    n
    -----
    -pp--
    -pp-e
    app-e
    apple 
    
    
"""
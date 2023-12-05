

# def sumnum(num1, num2):
#     res = num1 * num2
#     print(res)
#
#
# sumnum(2,2)
# sumnum(4,5)


""" Runtime error , exceptions  """

# num = int(input("please enter a number: "))
#
# print(num)

#
# try:
#     num = int(input("please enter a number: "))
#
#     print(num)
# except:
#     print("---- problem happened -----")
#
# print("------- after the explosion ---------------")




# try:
#     num = int(input("please enter a number: "))
#     print(name)
#     print(num)
# except Exception as e:
#     print(f"---- problem happened  {e}-----")
#
# print("------- after the explosion ---------------")
#

""" more than one except block """
# name = 'ahmed'
# try:
#     num = int(input("please enter a number: "))
#     print(name)
#     print(num)
# except NameError as ne:
#     print(f"---- variable not found  {ne}-----")
# except ValueError as ve:
#     print(f"---- value not suitable {ve}")
# except Exception as e:
#     print(f"----{e}")
#
# print("------- after the explosion ---------------")



""" else block """
# name = 'ahmed'
# try:
#     num1 = int(input("please enter first number: "))
#     num2  =  int(input("please enter second number: "))
#     res = num1  + num2
#
# except NameError as ne:
#     print(f"---- variable not found  {ne}-----")
# except ValueError as ve:
#     print(f"---- value not suitable {ve}")
# except Exception as e:
#     print(f"----{e}")
# else:
#
#     """ this block will be executed when there are no errors """
#     print(f"=== res = {res}")


""" finally """
# name = 'ahmed'
# try:
#     num1 = int(input("please enter first number: "))
#     num2  =  int(input("please enter second number: "))
#     res = num1  + num2
#
# except NameError as ne:
#     print(f"---- variable not found  {ne}-----")
# except ValueError as ve:
#     print(f"---- value not suitable {ve}")
# except Exception as e:
#     print(f"----{e}")
# else:
#
#     """ this block will be executed when there are no errors """
#     print(f"=== res = {res}")
#
# finally:
#     """ this block will be executed always """
#     print("---- we survived ==============")
#
#
# print("---------------------we survived ===-----------------------")


"""
    finally block ---> in side a function 
    finally block ---> priority is higher than return priority 

"""

# def askforInt(message):
#     while True:
#         try:
#             num = int(input("please enter a number : "))
#         except Exception as e:
#             print("---- invalid input ----")
#             # print(e)
#         else:
#             return  num
#         finally:
#             print("----- successfull operation -----")
#




# print(askforInt("please enter a number : "))




""" raising the exceptions """

from inputsmodule import  askforInt
def divnums():
    num1 = askforInt("please enter num1: ")
    num2 = askforInt("please enter num2: ")
    if num2==0:
        raise ValueError("num2 is zero , which is not valid ")
    print("---- divison process in progress ----")
    print(f"num1={num1}, num2={num2}")
    print("--- now check the result ---")
    res =num1/num2
    print(res)


divnums()









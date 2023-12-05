

# course = 'python'  # variable defined in python ---> variable with global scope
""" global scope variable can be accessed anywhere in the script after defining it """
# print(course)
# print(f"course= {course}")

""" variable defined inside a function """

# def saywelcome():
#     """ any variable defined inside a function  cannot be accessed outside"""
#     message = 'welcome to iti'
#     print(message)
#
# saywelcome()
# print('-----------------------')
# # print(message)

""" print global variable from inside the function """
# track = 'cybersecurity'
#
# def printTrack():
#     print(f"track = {track.upper()}")
#
# printTrack()


""" modify global variable from inside function """
coursename='python'

# def modify_course():
#     coursename = input('Enter course name: ')
#     print(f"from inside the function: {coursename}")
#
# modify_course()
# print(coursename)


# def modify_course():
#     global  coursename  # please don't create new local variable just use the global one
#     coursename = input('Enter course name: ')
#     print(f"from inside the function: {coursename}")
#
# modify_course()
# print(coursename)



""" define function inside another function """

# def outerfunction():
#     track = 'cybersecurity'  # local variable
#     """ you access local variable anywhere in the function """
#
#     """ print local variable  from inside function  """
#     def printTrack():
#         print(track.upper())
#
#     printTrack()
#     print(f"from  outerfunction track = {track}")
#
#
# outerfunction()
# print("------------------")


""" modify local variable from inside inner function """
# def outerfunction():
#     track = 'cybersecurity'  # local variable
#     """ you access local variable anywhere in the function """
#
#     """ print local variable  from inside function  """
#     def printTrack():
#         print(track.upper())
#
#     printTrack()
#     def modifyTrack():
#         track = input("please enter track name: ")  # new local variable
#         print(f"from modify function track= {track}")
#
#     modifyTrack()
#     print(f"from  outerfunction track = {track}")
#
#
# outerfunction()
# print("------------------")


def outerfunction():
    track = 'cybersecurity'  # local variable
    """ you access local variable anywhere in the function """

    """ print local variable  from inside function  """
    def printTrack():
        print(track.upper())

    printTrack()
    def modifyTrack():
        nonlocal track  # please don't create new local variable in the inner function
        track = input("please enter track name: ")  # new local variable
        print(f"from modify function track= {track}")

    modifyTrack()
    print(f"from  outerfunction track = {track}")


outerfunction()
print("------------------")



















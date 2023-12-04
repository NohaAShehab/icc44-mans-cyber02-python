

""" list datatype  can hold many values from different data types
"""
"1- to define a list "
l= []
myList = list()

"2- list can hold many values from different data types"
myl = ["Ahmed", 444, 444.55, None , 'iti', ["python", 'ccna', 'linux'], 'iti', 'test', True]
"3- access list elements using index "
print(myl[4])
print(myl[5][1])
# print(myl[20])  #IndexError: list index out of range

"""4- get len of list """
print(len(myl))

"5- count elements  in the list ? "
print(myl.count('iti'))

"6- list is mutable  data type ---> modify its content "
myl[3]=0  # update existing element in the list with new value
print(myl)

"7- append element to list -- add element to the end of the list"
myl.append("new element")
print(myl)

"8- insert element in specific index in the list ? "
myl.insert(4, 'inserted eleemnt')
print(myl)

"9- pop element from the list "
popped_element=myl.pop()
print(popped_element)
print(myl)

""" 10- pop element at specific index in the list ? """
popped_element = myl.pop(4)
print(popped_element)
print(myl)

"""11- sort list ---> You must make sure the list elements from the same type """
names= ["ahmed", "mazen", "Ashry", "abdelaziz", "aya", "Mariam", "Asmahan"]
print(names)
names.sort()  # sort the element in the same list --->  ascending
print(names)
""" sorted(names)"""
names.sort(reverse=True)
print(names)

"""12- reverse the list """
print(myl)
myl.reverse()
print(myl)

"""13- remove element form the list """
# myl.remove('iti') # remove first occurence of the element
# print(myl)
""" 14- get index of the element  --> get index of element in the list """
print(myl.index('iti'))

""" 15- loop over the list  """
for element in myl:
    print(f"element  = {element}")

"16- print index , element in the list "
for index, element in enumerate(myl):
    print(f"{index}:{element}")

"17- generate list of numbers ---> use range function ? "
nums  = range(1, 10, 2)
print(nums)

# for n in nums:
#     print(n)  # from start to end-1, accoding to the step

nums = list(nums)
print(nums)

"18- concatenate lists -"
l1 = ['eee', 'eee', 'rrr', 203]
l2= ['sd', 'djhf', 33,44.33]
l3 = l1 + l2
print(l3)  # new list

"""19- extend a list """
l1.extend(l2)
print(l1)

"20-check membership of element? "
print("sd" in l1)


"21- cast string to a list ? "
name='ahmed'
name = list(name)
print(name)

"22-convert list of string to one string ? "
values = ['test', 'name', 'email']
newvalues = ''.join(values)
print(newvalues)


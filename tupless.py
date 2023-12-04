# 
# 
""" tuple datatype  can hold many values from different data types
# """
"1- to define a tuple "
t= ()
mytuple = tuple()

# 
"2- tuple can hold many values from different data types"
myt = ("Ahmed", 444, 444.55, None , 'iti', ["python", 'ccna', 'linux'], ('iti', 'test'), True)
"3- access tuple elements using index "
print(myt[4])
print(myt[5][1])
# print(myt[20])  #IndexError: tuple index out of range
# 
"""4- get len of tuple """
print(len(myt))
# 
"5- count elements  in the tuple ? "
print(myt.count('iti'))
# 
"6- tuple is immutable  data type ---> you cannot modify its content "
# myt[3]=0# TypeError: 'tuple' object does not support item assignment




""" 7- loop over the tuple  """
for element in myt:
    print(f"element  = {element}")

"7- print index , element in the tuple "
for index, element in enumerate(myt):
    print(f"{index}:{element}")
# 
"8- generate tuple of numbers ---> use range function ? "
nums  = range(1, 10, 2)
print(nums)
nums = tuple(nums)
print(nums)
# 
"9- concatenate tuples -"
t1 = ('eee', 'eee', 'rrr', 203)
t2= ('sd', 'djhf', 33,44.33)
t3 = t1 + t2
print(t3)  # new tuple
# 

"10-check membership of element? "
print("sd" in t3)
# 
# 
"11- cast string to a tuple ? "
name='ahmed'
name = tuple(name)
print(name)
# 
"12-convert tuple of string to one string ? "
values = ('test', 'name', 'email')
newvalues = '#'.join(values)
print(newvalues)
#

"13- tuple of one item"
students= ('noha',)
print(students, type(students))

"14- min , max "
# print(min(t1)) #TypeError: '<' not supported between instances of 'int' and 'str'

data = ('ahmed', 'Ali', 'mohamed')
print(min(data))
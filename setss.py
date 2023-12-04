"set of the non primitive data types in python "

"1- define set "
s= set()
mys = {"Ahmed","iti", "ali", "iti", 44, 44.444, True, None, 1 }
print(mys)
"""
    un ordered data type
    remove duplication 
    no indices
"""

"2- mutable data type "
mys.add('added element')
print(mys)

"3- remove element from set "
popped = mys.pop()
print(popped)
print(mys)

mys.remove('iti')
print(mys)

"5- get len of set "
print(len(mys))

"6- set can hold only values from immutable data"

# mys= {"noha", 'ahmed', ['ccna', 'python', 'linux'], 55} #TypeError: unhashable type: 'list'
#
# print(mys)

mys= {"noha", 'ahmed', ('ccna', 'python', 'linux'), 55}
print(mys)

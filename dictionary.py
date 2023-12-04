

# info = ["noha", 31,'iti', 'Egyptian']  # unlabeled

# data type  --> description data

info = {}
myd = dict()

""" dict ? comma seperated key:value pairs """
info = {"name":'noha', 'work':'iti', 'age':31, 'name':"Noha Shehab"}
print(info)

"access element using key"
print(info['name'])

"modify elment using key"
info['work'] = 'Information Technology Institute'
print(info)

info['city']='Mansoura'
print(info)

""" pop element from dict using key """
popped_value = info.pop('age')
print(popped_value)

""" loop over the dict """
for item in info:  # item --> represent key
    print(f"item = {item}, {info[item]}")

""" get dict keys ?"""
keys = info.keys()  # dict_keys
print(keys)
""" dict_keys can be casted to a list """
keys_list =list(keys)
print(keys_list)

""" get dict values ? """
values = info.values()
print(values)
values_list = list(values)
print(values_list)

"""dict items"""

items = info.items()
print(items, type(items))
items_list = list(items)
print(items_list)

for k , v in info.items():
    print(f'{k}:{v}')

""" check element in dict ? """
print("Mansoura" in info )

""" clear """
# info.clear()  # remove all the key: value pairs in the dict

""" del """  # remove element from memeoy

del info['name']
print(info)

""" """

courses = {
    "cyber": ['python'],
    "ai": ['python', 'ml', 'linux'],
    'info': 5
}

branches = {
    "cairo": ['smart', 'nc', 'cu'],
    'upper': ['Menai', 'sohag'],
    'info': 7
}

courses.update(branches)
print(courses)
print(branches)

print(len(courses))
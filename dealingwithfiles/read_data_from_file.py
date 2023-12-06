
""" open file using read mode
    open file for reading starting from the beginning of file

"""
try:
    "1- open the file"
    fileobject = open("names.txt", 'r')  # TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobject)
    "2- read the data  "
    data = fileobject.read()  # read file content into one string
    print(data, type(data))

    """----- seek """
    res=fileobject.seek(0)  # reset file pointer to the beginning
    print(res)
    "3- read file lines"
    lines = fileobject.readlines()  # read file content into list --> line by line
    print(lines)
    """ check this """
    fileobject.seek(10)
    newlines = []
    for l in fileobject:
        newlines.append(l)

    print(newlines)

    fileobject.close()



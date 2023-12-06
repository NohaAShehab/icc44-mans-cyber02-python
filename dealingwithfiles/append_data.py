""" open file using append mode
    open file for appending  starting from the end of file
    if file doesn't exist , python will try to create it

    when you just open file with append mode ? keep old content

"""
try:
    "1- open the file"
    fileobject = open("dataa.txt", 'a')  # TextIOWrapper
except Exception as e:
    print(e)
else:

    print(fileobject)
    fileobject.write("we support Hamas \n")

    fileobject.writelines(['test\n', 'end\n', 'abc\n'])
    fileobject.close()

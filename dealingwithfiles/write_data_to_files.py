""" open file using write mode
    open file for writing starting from the beginning of file
    if file doesn't exist , python will try to create it

    when you just open file with write mode ? remove old content

"""
try:
    "1- open the file"
    fileobject = open("mycv.txt", 'w')  # TextIOWrapper
except Exception as e:
    print(e)
else:
    print(fileobject)

    fileobject.write("We support Hamas\n")
    fileobject.write("we support HAMAS\n")
    fileobject.write("-----------##############-------------\n")
    """ write lines """
    fileobject.writelines(['ahmed\n', 'mohamed\n', 'ali\n'])

    fileobject.close()

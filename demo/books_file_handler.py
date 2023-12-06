import  json

# saving data of the book

## check file empty or not ?

def read_all_books():
    try:
        fileobject = open("books_file.json", "r")
    except Exception as e:
        print(e)
        return False
    else:
        data = fileobject.read()
        # print(data)
        if data:
            data = json.loads(data)  # convert string to suitable python datatypes
        else:
            data = []
        fileobject.close()
        return data



def save_all_books(booksdata : list):
    booksdata = json.dumps(booksdata, indent=4)
    try:
        fileobject = open("books_file.json", 'w')
    except Exception as e:
        print(e)
        return  False
    else:
        fileobject.write(booksdata)
        return  True

def save_book(bookdata :dict ):
    # save book data to the list of the books ?
    allbooks = read_all_books() # list of dictionaries
    allbooks.append(bookdata)
    # print(allbooks)
    saved =save_all_books(allbooks)
    print(saved)


def search_by_id(book_id):
    allbooks = read_all_books()
    for book in allbooks:
        if book['id']==book_id:
            print("--- book found ")
            return  book
    else:
        print("--- book not found ")
        return  False



def delete_book_from_file(book):
    allbooks = read_all_books()
    if book in allbooks:
        allbooks.remove(book)
        saved = save_all_books(allbooks)
        print(saved)


if __name__ == "__main__":
    data=read_all_books()
    print(data)



"""
'[
  {"title": "book", "pages": 100},
{"title": "bookr", "pages": 99}

]'
"""
import  json
from demo.inputs_module import  askforInt, askforstring, generate_id
from demo.books_file_handler import  save_book, read_all_books, search_by_id, delete_book_from_file


def create_book():
    title = askforstring("please enter book title: ")
    pages  = askforInt("please enter number of pages: ")
    id = generate_id()
    book_data = {
        "id": id,
        "title":title,
        'pages': pages
    }

    # print(book_data)
    saved = save_book(book_data)
    print(saved)




def display_all_books():
    books  =read_all_books()
    for book in books:
        print(book)


def search_book():
    id = askforInt("please enter book id ")
    print(id)
    book=search_by_id(id)
    if book:
        print(book)
    return book




def delele_book():
    book = search_book()
    if book:
        print("--- delete book ")
        delete_book_from_file(book)



    # get all books , loop over them to check if book found or not
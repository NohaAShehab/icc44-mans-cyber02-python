from books_system import  create_book, display_all_books, search_book, delele_book


def main_project():
    while True:
        choice = input("""please enter n for new book ,
                       d for display, s for search ,  x for delete, all e for exit: """)
        if choice=='n':
            print("-- new book ---")
            create_book()
        elif choice=='d':
            display_all_books()
        elif choice=='s':
            search_book()
        elif choice=='x':
            delele_book()

        elif choice=='e':
            exit()

        else:
            print("---- please enter valid option -----")


if __name__ == '__main__':
    main_project()
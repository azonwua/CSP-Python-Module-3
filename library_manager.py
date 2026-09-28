from book import Book

def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    isbn = input("Enter the book ISBN: ")

    new_book = Book(title, author, isbn)
    library.append(new_book)

    print(f"Book '{new_book.title}' added to the library.")


def list_books(library):
    if not library:
        print("The library is empty.")
        return

    print("Books in the library:")
    for book in library:
        print(book.get_details())


def find_book(library):
    search_term = input("Enter the book title or ISBN to search: ").strip().lower()

    for book in library:
        if search_term in book.title.lower() or search_term == book.isbn.lower():
            print(book.get_details())
            return

    print("Book not found.")


my_library = []

while True:
    print("\nLibrary Manager")
    print("1. Add a book")
    print("2. List all books")
    print("3. Find a book")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_book(my_library)
    elif choice == '2':
        list_books(my_library)
    elif choice == '3':
        find_book(my_library)
    elif choice == '4':
        print("Exiting the Library Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
        
            